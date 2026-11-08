#!/usr/bin/env python3
"""Build or verify a reproducible, single-skill ZIP for direct downloads."""

import argparse
from io import BytesIO
from pathlib import Path
import re
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", help="Folder name under skills/")
    parser.add_argument("--check", action="store_true", help="Verify the ZIP matches the source")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.skill):
        parser.error("Use a skill folder name containing lowercase letters, numbers, and hyphens")

    root = Path(__file__).resolve().parent.parent
    source = root / "skills" / args.skill
    if source.is_symlink() or not (source / "SKILL.md").is_file():
        parser.error("The skill must be a local folder containing SKILL.md")

    buffer = BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            relative = path.relative_to(source)
            if any(part.startswith(".") or part == "__pycache__" for part in relative.parts):
                continue
            if path.is_symlink():
                parser.error(f"Cannot package a symlink: {relative}")
            if not path.is_file():
                continue
            entry = ZipInfo((Path(args.skill) / relative).as_posix(), (1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())

    destination = root / "downloads" / f"{args.skill}.zip"
    payload = buffer.getvalue()
    if args.check:
        if not destination.exists() or destination.read_bytes() != payload:
            print(f"Download is missing or stale. Run: python3 scripts/package-skill.py {args.skill}", file=sys.stderr)
            return 1
        print(f"Verified {destination.relative_to(root)} matches the skill source")
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        print(f"Created {destination.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
