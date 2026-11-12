#!/usr/bin/env python3
"""
i18n Parity and Synchronization Checker
Compares docs/ (English) and docs_es/ (Spanish) to report:
- Missing files in either language
- Files updated in one language that need translation sync in the other
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DOCS_EN = ROOT / "docs"
DOCS_ES = ROOT / "docs_es"

IGNORE_FILES = {".DS_Store", "Thumbs.db"}


def get_files(base: Path) -> dict[str, float]:
    """Return relative paths mapped to last modified timestamp."""
    files: dict[str, float] = {}
    if not base.exists():
        return files
    for p in base.rglob("*"):
        if p.is_file() and p.name not in IGNORE_FILES:
            rel = p.relative_to(base).as_posix()
            files[rel] = p.stat().st_mtime
    return files


def check_parity() -> int:
    en_files = get_files(DOCS_EN)
    es_files = get_files(DOCS_ES)

    missing_in_es = sorted(set(en_files) - set(es_files))
    missing_in_en = sorted(set(es_files) - set(en_files))

    both = set(en_files) & set(es_files)
    en_newer: list[str] = []
    es_newer: list[str] = []

    for rel in both:
        diff = en_files[rel] - es_files[rel]
        # Ignore sub-second filesystem discrepancies
        if diff > 2.0:
            en_newer.append(rel)
        elif diff < -2.0:
            es_newer.append(rel)

    print("=" * 60)
    print("🌍 Portfolio i18n Parity Report")
    print(f"English files (docs/):     {len(en_files)}")
    print(f"Spanish files (docs_es/):  {len(es_files)}")
    print("=" * 60)

    has_issues = False

    if missing_in_es:
        has_issues = True
        print("\n❌ Files present in English but MISSING in Spanish (docs_es/):")
        for f in missing_in_es:
            print(f"   - docs_es/{f}")

    if missing_in_en:
        has_issues = True
        print("\n❌ Files present in Spanish but MISSING in English (docs/):")
        for f in missing_in_en:
            print(f"   - docs/{f}")

    if en_newer:
        print("\n⚠️ Files updated in English after Spanish (review translation):")
        for f in sorted(en_newer):
            print(f"   - {f}")

    if es_newer:
        print("\n⚠️ Files updated in Spanish after English (review translation):")
        for f in sorted(es_newer):
            print(f"   - {f}")

    if not has_issues and not en_newer and not es_newer:
        print("\n✅ Perfect 1:1 parity between English and Spanish!")
        return 0

    return 1 if has_issues else 0


if __name__ == "__main__":
    sys.exit(check_parity())
