#!/usr/bin/env python3
"""Build a GitHub Release showcase.zip from converted Obsidrel content.

Only the 'resources/' YAML and 'pack/' assets are shipped. This script does
not generate runtime mappings, a catalog, or an installer for the Core.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ("resources", "pack")
ALLOWED_CATEGORIES = {
    "items", "blocks", "furniture", "entities", "armor-sets",
    "cosmetics", "actions", "conditions", "cooldowns", "triggers",
    "loot", "recipes", "fonts", "sounds", "variables",
}
UI_CATEGORIES = {"menus", "huds", "components"}
MAX_FILES = 10000
MAX_UNCOMPRESSED = 512 * 1024 * 1024
MAX_FILE = 64 * 1024 * 1024


def fail(message: str) -> None:
    raise SystemExit(f"Showcase release rejected: {message}")


def files_to_package() -> list[Path]:
    result: list[Path] = []
    total_size = 0

    for source in SOURCES:
        folder = ROOT / source
        if not folder.is_dir():
            fail(f"missing required folder: {source}/")
        for item in sorted(folder.rglob("*")):
            if item.is_symlink():
                fail(f"symlink forbidden: {item.relative_to(ROOT)}")
            if not item.is_file():
                continue
            relative = item.relative_to(ROOT)
            if any(part.startswith(".") for part in relative.parts):
                continue  # e.g. .gitkeep, OS metadata
            if item.stat().st_size > MAX_FILE:
                fail(f"file too large: {relative}")
            if source == "resources":
                if item.suffix.lower() not in (".yml", ".yaml"):
                    fail(f"non-YAML file in resources/: {relative}")
                parts = relative.parts
                recognized = (
                    len(parts) == 3 and parts[1] in ALLOWED_CATEGORIES
                ) or (
                    len(parts) == 4 and parts[1] == "ui"
                    and parts[2] in UI_CATEGORIES
                )
                if not recognized:
                    fail(f"unsupported YAML path: {relative}")
            total_size += item.stat().st_size
            if total_size > MAX_UNCOMPRESSED:
                fail("total uncompressed size exceeds 512 MiB")
            result.append(item)
            if len(result) > MAX_FILES:
                fail("too many files")

    if not any(p.relative_to(ROOT).parts[0] == "resources" for p in result):
        fail("at least one converted resource YAML is required")

    return result


def main() -> None:
    paths = files_to_package()
    target = ROOT / "showcase.zip"
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9,
                 allowZip64=True) as archive:
        for path in paths:
            relative = path.relative_to(ROOT).as_posix()
            info = ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)

    checksum = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / "showcase.sha256").write_text(
        f"{checksum}  showcase.zip\n", encoding="utf-8"
    )
    print(f"Packaged {len(paths)} files into showcase.zip (SHA-256 {checksum})")


if __name__ == "__main__":
    main()
