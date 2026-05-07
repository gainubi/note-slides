#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


FILES = [".gitignore", "LICENSE", "README.md", "SKILL.md", "template.html"]
DIRS = ["references", "scripts"]
BLOCKED = [
    re.compile(r"^output/"),
    re.compile(r"^dist/"),
    re.compile(r"^publish/"),
    re.compile(r"(^|/)__pycache__/"),
    re.compile(r"^wechat-article\.(md|html)$"),
    re.compile(r"^yuhao-dreame-.*\.html$"),
    re.compile(r"(^|/)\.DS_Store$"),
    re.compile(r"\.pyc$"),
    re.compile(r"\.slides\.html$"),
    re.compile(r"\.pptx$"),
    re.compile(r"\.mjs$"),
]


def main():
    parser = argparse.ArgumentParser(description="Pack core note slides skill files.")
    parser.add_argument("--root", default=os.getcwd())
    parser.add_argument("--output", default="")
    parser.add_argument("--git", action="store_true")
    parser.add_argument("--message", default="Keep note slides core files")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out_dir = Path(args.output).resolve() if args.output else Path(tempfile.mkdtemp(prefix="note-slides-core."))
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for file_name in FILES:
        copy_path(root / file_name, out_dir / file_name)
    for dir_name in DIRS:
        copy_dir(root / dir_name, out_dir / dir_name)

    packed = sorted(path.relative_to(out_dir).as_posix() for path in out_dir.rglob("*") if path.is_file())
    violations = [file for file in packed if any(pattern.search(file) for pattern in BLOCKED)]
    if violations:
        print("Pack contains blocked files:", file=sys.stderr)
        for file_name in violations:
            print(f"  {file_name}", file=sys.stderr)
        sys.exit(1)

    if args.git:
        run(["git", "init", "-b", "main"], out_dir)
        run(["git", "config", "user.name", "Codex"], out_dir)
        run(["git", "config", "user.email", "codex@openai.com"], out_dir)
        run(["git", "add", "-A"], out_dir)
        run(["git", "commit", "-m", args.message], out_dir)

    print(f"Packed {len(packed)} file(s) into {out_dir}")
    for file_name in packed:
        print(file_name)


def copy_path(source, target):
    if not source.exists() or should_skip(source):
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_dir(source, target):
    if not source.exists():
        return
    for item in source.iterdir():
        if should_skip(item):
            continue
        destination = target / item.name
        if item.is_dir():
            copy_dir(item, destination)
        else:
            copy_path(item, destination)


def should_skip(path):
    return path.name in {".DS_Store", "__pycache__"} or path.suffix == ".pyc"


def run(command, cwd):
    result = subprocess.run(command, cwd=cwd)
    if result.returncode:
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
