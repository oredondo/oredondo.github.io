#!/usr/bin/env python3
"""
Bilingual Development Server for Oscar Redondo's Portfolio
Builds and serves both English (/) and Spanish (/es/) versions on localhost:8000,
watching for file changes in docs/ and docs_es/ to rebuild automatically.
"""

from __future__ import annotations

import functools
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "site"
PORT = 8000

WATCH_DIRS = [ROOT / "docs", ROOT / "docs_es", ROOT / "overrides"]
WATCH_FILES = [ROOT / "mkdocs.yml", ROOT / "mkdocs.es.yml"]


def run_build(config_file: str | None = None) -> bool:
    """Run Zensical build for English (default) or Spanish."""
    cmd = ["uv", "run", "zensical", "build"]
    lang = "English (/)"
    if config_file:
        cmd.extend(["-f", config_file])
        lang = "Spanish (/es/)"

    try:
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  ✓ {lang} rebuilt successfully")
            return True
        else:
            print(f"  ✗ Error rebuilding {lang}:\n{res.stderr or res.stdout}")
            return False
    except Exception as e:
        print(f"  ✗ Failed to run build: {e}")
        return False


def build_both() -> None:
    print("🔨 Building dual portfolio with Zensical...")
    run_build()
    run_build("mkdocs.es.yml")
    print("✨ Dual build ready!\n")


def get_mtimes() -> dict[Path, float]:
    """Get modification timestamps of all tracked files."""
    mtimes: dict[Path, float] = {}
    for f in WATCH_FILES:
        if f.exists():
            mtimes[f] = f.stat().st_mtime
    for d in WATCH_DIRS:
        if d.exists():
            for p in d.rglob("*"):
                if p.is_file() and not p.name.startswith("."):
                    mtimes[p] = p.stat().st_mtime
    return mtimes


def file_watcher() -> None:
    """Watch for file changes and trigger targeted rebuilds."""
    last_mtimes = get_mtimes()
    while True:
        time.sleep(1.0)
        current_mtimes = get_mtimes()
        changed_paths = [
            p for p, mtime in current_mtimes.items()
            if p not in last_mtimes or mtime > last_mtimes[p]
        ]

        if changed_paths:
            rebuild_en = False
            rebuild_es = False

            for p in changed_paths:
                rel = str(p.relative_to(ROOT))
                print(f"📝 Changed: {rel}")
                if "docs_es" in rel or "mkdocs.es.yml" in rel:
                    rebuild_es = True
                elif "docs/" in rel or "mkdocs.yml" in rel:
                    rebuild_en = True
                else:
                    rebuild_en = True
                    rebuild_es = True

            if rebuild_en:
                run_build()
            if rebuild_es:
                run_build("mkdocs.es.yml")

            last_mtimes = current_mtimes


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def start_server(port: int = PORT) -> None:
    build_both()

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE_DIR))

    watcher_thread = threading.Thread(target=file_watcher, daemon=True)
    watcher_thread.start()

    print("=" * 65)
    print(f"🚀 Bilingual Dev Server running at: http://localhost:{port}/")
    print(f"   - 🇬🇧 English: http://localhost:{port}/")
    print(f"   - 🇪🇸 Spanish: http://localhost:{port}/es/")
    print("   - 🔄 Auto-reloading on changes in docs/ and docs_es/")
    print("   - Press Ctrl+C to stop")
    print("=" * 65 + "\n")

    try:
        with ReusableTCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped.")
        sys.exit(0)


if __name__ == "__main__":
    port_arg = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    start_server(port_arg)
