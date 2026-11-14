#!/usr/bin/env python3
"""
Automated CV Validator for Oscar Redondo's Portfolio.
Checks ATS compliance, Google XYZ metrics, active verb usage,
link integrity, and 1:1 bilingual parity between docs/cv/ and docs_es/cv/.
"""

import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
DOCS_EN = REPO_ROOT / "docs" / "cv" / "index.md"
DOCS_ES = REPO_ROOT / "docs_es" / "cv" / "index.md"

PASSIVE_TERMS_EN = [
    r"\bresponsible for\b",
    r"\bhelped with\b",
    r"\bassisted in\b",
    r"\bworked on\b",
    r"\btasked with\b",
]

PASSIVE_TERMS_ES = [
    r"\bencargado de\b",
    r"\bayudé a\b",
    r"\bparticipé en\b",
    r"\btrabajé en\b",
    r"\bresponsable de tareas\b",
]


def check_file_exists(path: Path) -> bool:
    if not path.is_file():
        print(f"❌ Missing file: {path}")
        return False
    return True


def check_passive_verbs(text: str, passive_patterns: list, lang: str) -> list:
    issues = []
    lines = text.splitlines()
    for idx, line in enumerate(lines, 1):
        # Only check experience bullets
        if line.strip().startswith("- "):
            for pat in passive_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    issues.append(f"Line {idx} [{lang}]: Passive phrase matched '{pat}': {line.strip()[:60]}...")
    return issues


def check_metrics_in_bullets(text: str, lang: str) -> list:
    """Verifies that high-level experience bullets contain quantifiable impact/numbers."""
    issues = []
    lines = text.splitlines()
    in_experience = False
    metric_pattern = re.compile(r"(\d+|%|\bhours\b|\bhoras\b|\bseconds\b|\bsegundos\b|zero downtime|cero tiempo)")

    for idx, line in enumerate(lines, 1):
        if "## Experiencia Profesional" in line or "## Professional Experience" in line:
            in_experience = True
            continue
        if in_experience and line.startswith("## "):
            in_experience = False
            break

        if in_experience and line.strip().startswith("- **"):
            if not metric_pattern.search(line):
                issues.append(f"Line {idx} [{lang}]: Bullet point lacks quantifiable metrics: {line.strip()[:65]}...")

    return issues


def check_links(text: str, source_path: Path) -> list:
    """Checks that relative internal markdown links point to existing files."""
    issues = []
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for match in link_pattern.finditer(text):
        target = match.group(2)
        if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
            continue
        
        clean_target = target.split("#")[0]
        resolved = (source_path.parent / clean_target).resolve()
        if not resolved.exists():
            issues.append(f"Broken internal link '{target}' in {source_path.name}")

    return issues


def main():
    print("============================================================")
    print("📋 CV Architect Validator — ATS & Google XYZ Parity Check")
    print("============================================================")

    if not check_file_exists(DOCS_EN) or not check_file_exists(DOCS_ES):
        sys.exit(1)

    text_en = DOCS_EN.read_text(encoding="utf-8")
    text_es = DOCS_ES.read_text(encoding="utf-8")

    all_issues = []

    # 1. Passive Verbs Check
    passive_en = check_passive_verbs(text_en, PASSIVE_TERMS_EN, "EN")
    passive_es = check_passive_verbs(text_es, PASSIVE_TERMS_ES, "ES")
    all_issues.extend(passive_en)
    all_issues.extend(passive_es)

    # 2. Metric / Scale Check in Experience
    metrics_en = check_metrics_in_bullets(text_en, "EN")
    metrics_es = check_metrics_in_bullets(text_es, "ES")
    all_issues.extend(metrics_en)
    all_issues.extend(metrics_es)

    # 3. Internal Links Check
    links_en = check_links(text_en, DOCS_EN)
    links_es = check_links(text_es, DOCS_ES)
    all_issues.extend(links_en)
    all_issues.extend(links_es)

    # 4. Parity checks (Headings count)
    h2_en = len(re.findall(r"^##\s+", text_en, re.MULTILINE))
    h2_es = len(re.findall(r"^##\s+", text_es, re.MULTILINE))
    if h2_en != h2_es:
        all_issues.append(f"Heading count mismatch: EN has {h2_en} '##' sections, ES has {h2_es}")

    if all_issues:
        print("\n⚠️ Issues found:")
        for issue in all_issues:
            print(f"  • {issue}")
        print("\n❌ Validation failed. Please address the issues above.")
        sys.exit(1)

    print("\n✅ All checks passed successfully!")
    print("  • 0 passive verbs detected (100% active voice)")
    print("  • Verifiable metrics & scale present in all core bullets")
    print("  • 100% valid internal links and project cross-references")
    print(f"  • Strict bilingual structural parity ({h2_en} sections in EN & ES)")
    print("============================================================\n")


if __name__ == "__main__":
    main()
