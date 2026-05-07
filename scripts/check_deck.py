#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Check generated note slides HTML.")
    parser.add_argument("--input", "-i", required=True)
    args = parser.parse_args()

    html = Path(args.input).read_text(encoding="utf-8")
    errors = []
    warnings = []
    slide_blocks = re.findall(r"<section\b[^>]*class=[\"'][^\"']*\bslide\b[^\"']*[\"'][^>]*>[\s\S]*?</section>", html, flags=re.I)
    sections = [
        re.match(r"<section\b[^>]*>", block, flags=re.I).group(0)
        for block in slide_blocks
        if re.match(r"<section\b[^>]*>", block, flags=re.I)
    ]
    forbidden = [
        r"\[必填]",
        r"\[内容]",
        r"TODO",
        r"lorem ipsum",
        r"假数据",
        r"大面积渐变",
        "\u2014",
    ]
    vague = [
        r"这(篇|期|次).{0,8}(真正|本质|核心)讲的是",
        r"本质上是在说",
        r"最该带走的是",
        r"路转粉|太精彩|值得学习",
    ]

    if not sections:
        errors.append("No slide sections found.")

    for index, section in enumerate(sections, start=1):
        label = f"slide {index}"
        for attr in ["data-theme", "data-screen-label", "data-source"]:
            if not has_attr(section, attr):
                errors.append(f"{label}: missing {attr}.")
        source = attr_value(section, "data-source")
        if not source or re.search(r"\[|必填|TODO", source, flags=re.I):
            errors.append(f"{label}: invalid data-source.")
        theme = attr_value(section, "data-theme")
        if theme and theme not in ["dark", "light"]:
            warnings.append(f"{label}: uncommon data-theme {theme}.")
    for index, block in enumerate(slide_blocks, start=1):
        label = f"slide {index}"
        visible = strip_tags(block)
        headings = heading_texts(block)
        callouts = callout_texts(block)
        stat_count = len(re.findall(r"class=[\"'][^\"']*\bstat-num\b", block, flags=re.I))
        has_three_column = bool(re.search(r"class=[\"'][^\"']*\bgrid-3\b", block, flags=re.I))
        has_table = bool(re.search(r"<table\b", block, flags=re.I))
        mixed_signals = sum(bool(re.search(pattern, visible)) for pattern in [r"\d+\s*%", r"\d+\s*年|\d{4}年", r"扫地机|吸尘器|汽车|手机|大家电"])
        for heading in headings:
            display_len = visual_length(heading)
            if display_len > 34 and (stat_count or (has_three_column and mixed_signals > 1)):
                warnings.append(f"{label}: long heading combined with grid or stat blocks. Split biography, metrics, and product scope into quieter structures.")
        if stat_count > 1:
            warnings.append(f"{label}: multiple stat-num blocks. Use only for comparable metrics, otherwise table, timeline, or split pages.")
        if has_three_column and mixed_signals > 1:
            warnings.append(f"{label}: three-column layout mixes biography, time, percentage, or product scope. Use table, timeline, or split pages.")
        for quote in callouts + headings:
            quote_len = visual_length(quote)
            if quote_len > 72 and has_three_column:
                warnings.append(f"{label}: long quote or headline above a three-column block. Split quote and explanation into separate slides.")
            elif quote_len > 72 and re.search(r"class=[\"'][^\"']*\bcallout\b", block, flags=re.I):
                warnings.append(f"{label}: oversized quote is too long. Use excerpt layout, smaller text, or split the quote.")
        if stat_count and re.search(r"\d+\s*%|\d+\s*年|\d{4}年|扫地机|吸尘器|汽车|手机|大家电", visible):
            if mixed_signals > 1:
                warnings.append(f"{label}: mixed metric types near large numbers. Do not give percentage, time, and product scope equal visual weight.")
        if has_table:
            if not re.search(r"class=[\"'][^\"']*\btable-wrap\b", block, flags=re.I):
                warnings.append(f"{label}: table found without table-wrap. Use the template table layout.")
            if not re.search(r"class=[\"'][^\"']*\bdata-table\b", block, flags=re.I):
                warnings.append(f"{label}: table found without data-table class. Avoid custom table styling.")
            centered_table_group = re.search(r"class=[\"'][^\"']*\bslide-body\b", block, flags=re.I) or re.search(r"justify-content\s*:\s*center", block, flags=re.I)
            if not centered_table_group:
                warnings.append(f"{label}: table should sit inside slide-body so title and table center as one group.")

    title = tag_text(html, "title")
    if not title or re.search(r"必填|TODO", title):
        errors.append("Missing or placeholder <title>.")
    for pattern in forbidden:
        if re.search(pattern, html, flags=re.I):
            errors.append(f"Forbidden placeholder or wording found: {pattern}")
    stripped = strip_tags(html)
    for pattern in vague:
        if re.search(pattern, stripped):
            warnings.append(f"Possible guide wording: {pattern}")
    if "localStorage" not in html:
        warnings.append("Progress persistence not found.")
    if not re.search(r"querySelectorAll\([\"']\.slide[\"']\)", html):
        warnings.append("Slide navigation script may be missing.")
    if re.search(r"<img\b", html, flags=re.I) and not re.search(r"<figure\b[^>]*class=[\"'][^\"']*\bslide-img\b", html, flags=re.I):
        warnings.append("Images found without figure.slide-img wrapper.")
    css = css_only(html)
    if re.search(r"aspect-ratio\s*:", html, flags=re.I):
        errors.append("aspect-ratio is forbidden for slide images.")
    if re.search(r"font-size\s*:\s*(?!\s*clamp\()[^;]+;", css, flags=re.I):
        warnings.append("Some CSS font-size declarations do not use clamp().")
    if re.search(r"text-align\s*:\s*right", css, flags=re.I):
        warnings.append("Right-aligned text detected. Content text should be left-aligned or centered except page chrome or numeric table columns.")
    if re.search(r"border-radius\s*:\s*(1[2-9]|[2-9]\d)px", css, flags=re.I):
        warnings.append("Large border-radius detected.")
    quote_count = len(re.findall(r"[“”\"「」『』]", strip_tags(html)))
    if sections and quote_count / len(sections) > 4:
        warnings.append(f"High quote density detected: {quote_count} quote marks across {len(sections)} slides.")
    if len(sections) >= 20 and not re.search(r"核心总结|Core Notes", stripped, flags=re.I):
        warnings.append("Long deck may be missing core summary pages near the end.")

    nav_dots = len(re.findall(r"class=[\"'][^\"']*\bdot\b", html, flags=re.I))
    if nav_dots and nav_dots != len(sections):
        warnings.append(f"Static nav dots {nav_dots} do not match sections {len(sections)}.")

    report(errors, warnings, f"Deck check passed: {len(sections)} slide(s), {len(warnings)} warning(s).")


def has_attr(tag, name):
    return bool(re.search(rf"\s{name}=[\"'][^\"']+[\"']", tag, flags=re.I))


def attr_value(tag, name):
    matched = re.search(rf"\s{name}=[\"']([^\"']*)[\"']", tag, flags=re.I)
    return matched.group(1) if matched else ""


def tag_text(content, tag_name):
    matched = re.search(rf"<{tag_name}[^>]*>([\s\S]*?)</{tag_name}>", content, flags=re.I)
    return matched.group(1) if matched else ""


def strip_tags(content):
    content = re.sub(r"<script[\s\S]*?</script>", " ", content, flags=re.I)
    content = re.sub(r"<style[\s\S]*?</style>", " ", content, flags=re.I)
    return re.sub(r"<[^>]+>", " ", content)


def heading_texts(content):
    results = []
    for matched in re.findall(r"<h[1-3]\b[^>]*>([\s\S]*?)</h[1-3]>", content, flags=re.I):
        text = re.sub(r"<[^>]+>", " ", matched)
        text = re.sub(r"\s+", "", text)
        if text:
            results.append(text)
    return results


def callout_texts(content):
    results = []
    for matched in re.findall(r"<(?:div|blockquote)\b[^>]*class=[\"'][^\"']*\bcallout\b[^\"']*[\"'][^>]*>([\s\S]*?)</(?:div|blockquote)>", content, flags=re.I):
        text = re.sub(r"<cite[\s\S]*?</cite>", " ", matched, flags=re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", "", text)
        if text:
            results.append(text)
    return results


def visual_length(text):
    total = 0
    for char in text:
        if re.match(r"[\u4e00-\u9fff]", char):
            total += 2
        elif char.strip():
            total += 1
    return total


def css_only(content):
    return "\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", content, flags=re.I))


def report(errors, warnings, success_message):
    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    print(success_message)


if __name__ == "__main__":
    main()
