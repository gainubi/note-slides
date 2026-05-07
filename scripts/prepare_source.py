#!/usr/bin/env python3
import argparse
import datetime as dt
import html
import json
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Prepare source material for note slides.")
    parser.add_argument("--input", "-i", required=True, help="Input md/html/text file.")
    parser.add_argument("--output", "-o", default="source.json", help="Output source JSON.")
    args = parser.parse_args()

    input_path = Path(args.input)
    raw = input_path.read_text(encoding="utf-8")
    html_like = input_path.suffix.lower() == ".html" or re.search(r"<html[\s>]|<article[\s>]", raw, re.I)
    text = clean_text(html_to_text(raw) if html_like else markdown_to_text(raw))
    blocks = split_blocks(text)

    source = {
        "version": 1,
        "generatedAt": dt.datetime.now(dt.UTC).isoformat(),
        "input": str(input_path.resolve()),
        "meta": {
            **extract_meta(raw, input_path, html_like),
            "charCount": len(text),
            "blockCount": len(blocks),
            "validation": detect_wechat_validation(raw),
        },
        "blocks": [classify_block(content, index) for index, content in enumerate(blocks)],
    }
    source["candidates"] = {
        "headings": [candidate(block) for block in source["blocks"] if block["type"] == "heading"],
        "questions": [candidate(block) for block in source["blocks"] if block["signals"]["question"]],
        "numbers": [candidate(block) for block in source["blocks"] if block["signals"]["number"]],
        "heavyLines": [candidate(block) for block in source["blocks"] if block["signals"]["heavyLine"]],
    }

    Path(args.output).write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}")
    print(f"{source['meta'].get('title') or input_path.name} · {source['meta']['charCount']} chars · {source['meta']['blockCount']} blocks")
    if source["meta"]["validation"]["isValidationPage"]:
        print("Warning: possible WeChat validation page. Do not generate slides from this source.")


def detect_wechat_validation(content):
    patterns = ["环境异常", "完成验证后即可继续访问", "去验证", "请在微信客户端打开链接"]
    hits = [pattern for pattern in patterns if pattern in content]
    return {"isValidationPage": bool(hits), "hits": hits}


def extract_meta(content, input_path, html_like):
    title = (
        find(content, r"^#\s+(.+)$", re.M)
        or find(content, r"<meta[^>]+property=[\"']og:title[\"'][^>]+content=[\"']([^\"']+)[\"']", re.I)
        or find(content, r"<title[^>]*>([\s\S]*?)</title>", re.I)
        or input_path.name
    )
    author = (
        find(content, r"^Author:\s*(.+)$", re.I | re.M)
        or find(content, r"var\s+nickname\s*=\s*[\"']([^\"']+)[\"']", re.I)
        or find(content, r"id=[\"']js_name[\"'][^>]*>([\s\S]*?)</[^>]+>", re.I)
    )
    published_at = (
        find(content, r"^Published:\s*(.+)$", re.I | re.M)
        or find(content, r"var\s+ct\s*=\s*[\"']([^\"']+)[\"']", re.I)
        or find(content, r"publish_time[^>]*>([\s\S]*?)</[^>]+>", re.I)
    )
    url = (
        find(content, r"^Source URL:\s*(.+)$", re.I | re.M)
        or find(content, r"<meta[^>]+property=[\"']og:url[\"'][^>]+content=[\"']([^\"']+)[\"']", re.I)
    )
    return {
        "title": clean_inline(html.unescape(title or "")),
        "author": clean_inline(html.unescape(author or "")),
        "publishedAt": clean_inline(html.unescape(published_at or "")),
        "url": clean_inline(html.unescape(url or "")),
        "inputType": "html" if html_like else "text",
    }


def find(content, pattern, flags=0):
    matched = re.search(pattern, content, flags)
    return matched.group(1) if matched else ""


def html_to_text(content):
    body = (
        find(content, r"<div[^>]+id=[\"']js_content[\"'][^>]*>([\s\S]*?)</div>\s*<script", re.I)
        or find(content, r"<article[^>]*>([\s\S]*?)</article>", re.I)
        or find(content, r"<body[^>]*>([\s\S]*?)</body>", re.I)
        or content
    )
    body = re.sub(r"<script[\s\S]*?</script>", "\n", body, flags=re.I)
    body = re.sub(r"<style[\s\S]*?</style>", "\n", body, flags=re.I)
    body = re.sub(r"<(h[1-6]|p|div|section|article|blockquote|li|br)[^>]*>", "\n", body, flags=re.I)
    body = re.sub(r"<[^>]+>", "", body)
    return html.unescape(body.replace("\u200b", ""))


def markdown_to_text(content):
    content = re.sub(r"^Source URL:\s*.+$", "", content, flags=re.I | re.M)
    content = re.sub(r"^Author:\s*.+$", "", content, flags=re.I | re.M)
    content = re.sub(r"^Published:\s*.+$", "", content, flags=re.I | re.M)
    content = re.sub(r"!\[[^\]]*]\([^)]+\)", "", content)
    content = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", content)
    content = re.sub(r"`([^`]+)`", r"\1", content)
    return re.sub(r"^\s{0,3}#{1,6}\s+", "# ", content, flags=re.M)


def clean_text(content):
    content = html.unescape(content)
    content = content.replace("\r", "").replace("\t", " ")
    content = re.sub(r"[ \u00a0]+", " ", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip()


def clean_inline(content):
    return re.sub(r"\s+", " ", str(content)).strip()


def split_blocks(content):
    blocks = []
    for block in re.split(r"\n{2,}", content):
        block = re.sub(r"\n+", "\n", block).strip()
        if not block:
            continue
        blocks.extend(split_long_block(block) if len(block) > 420 else [block])
    return blocks


def split_long_block(block):
    sentences = [item for item in re.split(r"(?<=[。！？!?])\s*", block) if item]
    out = []
    current = ""
    for sentence in sentences:
        if len(current + sentence) > 360 and current:
            out.append(current.strip())
            current = ""
        current += sentence
    if current.strip():
        out.append(current.strip())
    return out


def classify_block(content, index):
    normalized = re.sub(r"^#\s*", "", content).strip()
    prefix = "q" if looks_like_question(normalized) else "h" if looks_like_heading(content) else "p"
    signals = {
        "question": looks_like_question(normalized),
        "number": bool(re.search(r"(\d+([.,]\d+)?%?|\d+\s*(年|月|日|万|亿|倍|小时|分钟|Token|token))", normalized, re.I)),
        "heavyLine": looks_heavy(normalized),
    }
    return {
        "id": f"{prefix}{index + 1:03d}",
        "type": "heading" if looks_like_heading(content) else "question" if signals["question"] else "paragraph",
        "text": normalized,
        "charCount": len(normalized),
        "signals": signals,
    }


def looks_like_heading(content):
    line = content.strip()
    if line.startswith("# "):
        return True
    return len(line) <= 28 and not re.search(r"[。！？!?]$", line) and not re.search(r"[，,；;]", line)


def looks_like_question(content):
    return bool(re.search(r"[？?]\s*$", content) or re.search(r"^(为什么|怎么|如何|是不是|能不能|什么是|谁|哪|是否)", content))


def looks_heavy(content):
    if len(content) > 120:
        return False
    return bool(re.search(r"(不是|而是|不能|必须|真正|关键|核心|本质|意味着|决定|改变|重写|失败|成功|边界|规律|方法)", content))


def candidate(block):
    return {"id": block["id"], "type": block["type"], "text": block["text"][:120]}


if __name__ == "__main__":
    main()
