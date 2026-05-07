#!/usr/bin/env python3
import argparse
from collections import Counter
import json
import re
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Check a note slides plan.")
    parser.add_argument("--plan", "-p", default="deck.plan.json")
    parser.add_argument("--source", "-s", default="source.json")
    args = parser.parse_args()

    plan = read_json(args.plan)
    source = read_json(args.source) if Path(args.source).exists() else None
    slides = plan.get("slides") if isinstance(plan.get("slides"), list) else []
    source_ids = {block["id"] for block in source.get("blocks", [])} if source else set()
    allowed_layouts = {f"L{number}" for number in range(1, 33)}
    layouts = [str(slide.get("layout", "")).upper() for slide in slides]
    layout_counts = Counter(layout for layout in layouts if layout)
    errors = []
    warnings = []
    vague_patterns = [
        r"这(篇|期|次).{0,8}(真正|本质|核心)讲的是",
        r"本质上是在说",
        r"最该带走的是",
        r"外界看到.*解释为什么",
        r"一种.+方法论$",
        r"路转粉|太精彩|值得学习",
    ]

    if not isinstance(plan.get("slides"), list):
        errors.append("plan.slides must be an array.")
    if len(slides) < 6:
        warnings.append(f"Only {len(slides)} slides. Confirm this is intentional.")
    if len(slides) > 40:
        warnings.append(f"Too many slides: {len(slides)}. Consider splitting the deck.")
    if len(slides) >= 10:
        minimum_layouts = 6
        used_layouts = len(set(layouts) - {""})
        if used_layouts < minimum_layouts:
            warnings.append(f"Only {used_layouts} distinct layouts. Use at least {minimum_layouts} unless the deck is an intentional series.")
    if layout_counts["L9"]:
        allowed_l9 = max(2, min(4, round(len(slides) * 0.12)))
        if layout_counts["L9"] > allowed_l9:
            warnings.append(f"L9 appears {layout_counts['L9']} times. Keep title plus three-column pages to about 12 percent of the deck.")

    for index, slide in enumerate(slides, start=1):
        label = f"slide {index}"
        ids = slide.get("sourceIds")
        if not isinstance(ids, list) or not ids:
            errors.append(f"{label}: sourceIds is required.")
        elif source:
            for source_id in ids:
                if source_id not in source_ids:
                    errors.append(f"{label}: unknown sourceId {source_id}.")
        if not (slide.get("sourceLabel") or slide.get("source")):
            errors.append(f"{label}: sourceLabel is required.")
        if not slide.get("screenLabel"):
            errors.append(f"{label}: screenLabel is required.")
        layout = str(slide.get("layout", "")).upper()
        if not layout:
            errors.append(f"{label}: layout is required.")
        elif layout not in allowed_layouts:
            errors.append(f"{label}: unknown layout {slide.get('layout')}.")
        if not slide.get("point"):
            errors.append(f"{label}: point is required.")
        if not slide.get("anchor"):
            errors.append(f"{label}: anchor is required.")
        text = " ".join(str(slide.get(key, "")) for key in ["point", "anchor", "note", "sourceLabel"])
        for pattern in vague_patterns:
            if re.search(pattern, text):
                errors.append(f"{label}: vague guide wording detected: {pattern}")
        if "\u2014" in text:
            errors.append(f"{label}: em dash is not allowed.")

    for index in range(1, len(slides)):
        if slides[index].get("layout") == slides[index - 1].get("layout") and not slides[index].get("series"):
            warnings.append(f"slides {index} and {index + 1}: same layout {slides[index].get('layout')}. Mark series=true if intentional.")
        if layouts[index] == "L9" and layouts[index - 1] == "L9" and not slides[index].get("series"):
            warnings.append(f"slides {index} and {index + 1}: consecutive L9 pages. Use L25, L26, L27, L28, L16, or L30 unless this is a true three-part series.")

    for index in range(2, len(slides)):
        themes = [theme_of(slides[index - offset]) for offset in [2, 1, 0]]
        if themes[0] and themes[0] == themes[1] == themes[2]:
            warnings.append(f"slides {index - 1}-{index + 1}: three consecutive {themes[0]} themes.")
    if len(slides) >= 20 and not any(str(slide.get("layout", "")).upper() == "L32" for slide in slides[-6:]):
        warnings.append("Long deck does not include L32 core summary near the end.")

    report(errors, warnings, f"Plan check passed with {len(warnings)} warning(s).")


def read_json(file_path):
    try:
        return json.loads(Path(file_path).read_text(encoding="utf-8"))
    except Exception as error:
        print(f"Cannot read JSON: {file_path}", file=sys.stderr)
        print(str(error), file=sys.stderr)
        sys.exit(1)


def theme_of(slide):
    return slide.get("theme") or slide.get("dataTheme") or ""


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
