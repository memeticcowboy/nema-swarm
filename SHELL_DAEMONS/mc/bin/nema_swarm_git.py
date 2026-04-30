#!/usr/bin/env python3
"""
nema_swarm_git.py — shared helper for publishing to memeticcowboy/nema-swarm.

[REBUILT 2026-04-28 from session history + patches doc, after MC's
 destructive "pause Daily Encounters" cleanup wiped the original.
 Incorporates every fix landed today:
   • REPO moved out of ~/Documents/ (TCC blocked launchd processes)
   • push_siml_term symlink-overlap detection (when src/dst resolve to the
     same physical path through the Phase 1 symlink, skip rmtree+copytree
     and let git add work directly on the in-place files)]

Used by:
  - bin/poll-encode-channel.py        → SIML term push after @MC encoding
  - bin/encode-winning-idea.py        → SIML term push after CTA winner
  - bin/arc-tick.py (Newsletter act)  → blog post push to docs/blog/posts/

Canonical local clone:   /Users/nema/repos/nema-swarm
                         (moved from ~/Documents/GitHub/nema-swarm 2026-04-28
                          because macOS TCC blocks launchd processes from
                          accessing ~/Documents/)
Git remote (HTTPS):      https://github.com/memeticcowboy/nema-swarm.git
Auth:                    osxkeychain + ~/.git-credentials (already configured)

All ops serialized through a filelock so concurrent cron jobs don't stomp.
Pull-before-push is always attempted to avoid fast-forward conflicts.

Public URLs returned:
  - SIML term:  https://github.com/memeticcowboy/nema-swarm/tree/main/SIML/terms/<dir>
  - Blog post:  https://memeticcowboy.github.io/nema-swarm/blog/posts/<slug>/

CLI:
  nema_swarm_git.py push-term <term_dir_name>
  nema_swarm_git.py push-blog <markdown_path> [--audio <audio_dir>]
  nema_swarm_git.py pull        # explicit pull (otherwise auto on each op)
"""

from __future__ import annotations

import datetime as dt
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

REPO = Path(os.path.expanduser("~/repos/nema-swarm"))
VAULT_TERMS = Path(os.path.expanduser("~/.openclaw/workspace/SIML/terms"))
REPO_TERMS = REPO / "SIML/terms"
REPO_BLOG_POSTS = REPO / "docs/blog/posts"
REPO_BLOG_AUDIO = REPO / "docs/blog/audio"
LOCK_FILE = Path(os.path.expanduser("~/.openclaw/workspace/SHELL_DAEMONS/mc/ledger/nema-swarm-git.lock"))
LOG = Path(os.path.expanduser("~/.openclaw/workspace/SHELL_DAEMONS/mc/channel-logs/nema-swarm-git.log"))

BRANCH = "main"
REPO_URL_TREE = "https://github.com/memeticcowboy/nema-swarm/tree/main"
PAGES_URL = "https://memeticcowboy.github.io/nema-swarm"


def _log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a") as f:
        f.write(f"[{dt.datetime.utcnow().isoformat()}Z] {msg}\n")


def _run(args, check: bool = False, timeout: int = 120) -> subprocess.CompletedProcess:
    r = subprocess.run(args, cwd=REPO, capture_output=True, text=True, timeout=timeout)
    if check and r.returncode != 0:
        _log(f"cmd failed rc={r.returncode}: {' '.join(args[:5])}... stderr={r.stderr.strip()[:300]}")
        raise RuntimeError(f"git op failed: {r.stderr.strip()[:200]}")
    return r


@contextmanager
def _locked():
    """Filelock so concurrent cron jobs don't stomp each other."""
    LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(LOCK_FILE), os.O_CREAT | os.O_RDWR, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _pull() -> bool:
    """Pull origin/main with rebase. Returns True if successful."""
    r = _run(["git", "pull", "--rebase", "--autostash", "origin", BRANCH], timeout=120)
    if r.returncode != 0:
        _log(f"pull failed: {r.stderr.strip()[:300]}")
        return False
    return True


def _commit_and_push(paths: list, message: str) -> bool:
    """Stage paths, commit, push. Idempotent — returns True if nothing to stage."""
    add = _run(["git", "add", *paths])
    if add.returncode != 0:
        _log(f"git add failed: {add.stderr.strip()[:200]}")
        return False
    # Check if anything staged
    st = _run(["git", "diff", "--cached", "--quiet"])
    if st.returncode == 0:
        _log(f"nothing staged (paths already in tree): {paths}")
        return True  # idempotent success
    commit = _run(["git", "commit", "-m", message])
    if commit.returncode != 0:
        _log(f"git commit failed: {commit.stderr.strip()[:200]}")
        return False
    push = _run(["git", "push", "origin", BRANCH], timeout=120)
    if push.returncode != 0:
        _log(f"git push failed: {push.stderr.strip()[:300]}")
        return False
    return True


def push_siml_term(term_dir_name: str) -> dict:
    """Publish SIML/terms/<dir> from the local vault to the repo and push.

    After the Phase 1 simlab migration (2026-04-27), VAULT_TERMS may be a
    symlink into REPO_TERMS — in which case src and dst resolve to the same
    physical directory. We detect that case and skip the copytree/rmtree
    dance (which would delete the just-written term and then fail on the copy).

    Returns: {ok, url, repo_path, pushed}
    """
    src = VAULT_TERMS / term_dir_name
    if not src.is_dir():
        return {"ok": False, "error": f"vault term dir missing: {src}"}
    dst = REPO_TERMS / term_dir_name

    with _locked():
        if not REPO.exists():
            return {"ok": False, "error": f"repo missing: {REPO}"}
        _pull()

        # Detect symlink overlap: src and dst resolve to the same physical path.
        try:
            same_location = src.resolve() == dst.resolve() if dst.exists() else (
                src.resolve() == (dst.parent.resolve() / dst.name)
            )
        except Exception:
            same_location = False

        if not same_location:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            _log(f"vault and repo are same physical location for {term_dir_name}; skipping copytree (already in working tree)")

        pushed = _commit_and_push(
            [f"SIML/terms/{term_dir_name}"],
            f"simlab: add {term_dir_name}",
        )

    return {
        "ok": pushed,
        "url": f"{REPO_URL_TREE}/SIML/terms/{term_dir_name}",
        "repo_path": f"SIML/terms/{term_dir_name}",
        "pushed": pushed,
    }


_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def _slugify(text: str, max_words: int = 10) -> str:
    words = _SLUG_STRIP.sub("-", text.lower()).strip("-").split("-")
    words = [w for w in words if w][:max_words]
    return "-".join(words) or "untitled"


def push_blog_post(markdown_path: str, audio_dir: Optional[str] = None,
                   slug: Optional[str] = None) -> dict:
    """Copy a blog post (and optional audio dir) into docs/blog/ and push.

    If `slug` is None, derives one from the markdown's H1 title or filename.
    """
    md_src = Path(markdown_path).expanduser().resolve()
    if not md_src.is_file():
        return {"ok": False, "error": f"markdown not found: {md_src}"}

    if slug is None:
        # Try H1 first
        text = md_src.read_text()
        m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        slug = _slugify(m.group(1)) if m else _slugify(md_src.stem)

    # Prefix with today's date if not already date-prefixed
    if not re.match(r"^\d{4}-\d{2}-\d{2}-", slug):
        slug = f"{dt.date.today().isoformat()}-{slug}"

    md_dst = REPO_BLOG_POSTS / f"{slug}.md"
    paths_to_stage = [f"docs/blog/posts/{slug}.md"]

    with _locked():
        if not REPO.exists():
            return {"ok": False, "error": f"repo missing: {REPO}"}
        _pull()

        REPO_BLOG_POSTS.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_src, md_dst)

        if audio_dir:
            audio_src = Path(audio_dir).expanduser().resolve()
            if audio_src.is_dir():
                audio_dst = REPO_BLOG_AUDIO / slug
                if audio_dst.exists():
                    shutil.rmtree(audio_dst)
                shutil.copytree(audio_src, audio_dst)
                paths_to_stage.append(f"docs/blog/audio/{slug}")

        pushed = _commit_and_push(
            paths_to_stage,
            f"blog: {slug}",
        )

    return {
        "ok": pushed,
        "url": f"{PAGES_URL}/blog/posts/{slug}",
        "repo_path": f"docs/blog/posts/{slug}.md",
        "pushed": pushed,
    }


def ensure_gitattributes_lfs() -> dict:
    """Ensure .gitattributes has LFS rules for audio formats. Idempotent."""
    gitattr = REPO / ".gitattributes"
    needed = [
        "*.mp3 filter=lfs diff=lfs merge=lfs -text",
        "*.ogg filter=lfs diff=lfs merge=lfs -text",
        "*.wav filter=lfs diff=lfs merge=lfs -text",
        "*.m4a filter=lfs diff=lfs merge=lfs -text",
    ]
    existing = gitattr.read_text() if gitattr.is_file() else ""
    missing = [line for line in needed if line not in existing]
    if not missing:
        return {"ok": True, "added": []}
    with _locked():
        with open(gitattr, "a") as f:
            if existing and not existing.endswith("\n"):
                f.write("\n")
            for line in missing:
                f.write(line + "\n")
        pushed = _commit_and_push([".gitattributes"], "lfs: add audio extensions")
    return {"ok": pushed, "added": missing}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 1
    cmd = sys.argv[1]
    if cmd == "push-term":
        if len(sys.argv) < 3:
            print(json.dumps({"ok": False, "error": "missing term_dir_name"}))
            return 1
        r = push_siml_term(sys.argv[2])
    elif cmd == "push-blog":
        if len(sys.argv) < 3:
            print(json.dumps({"ok": False, "error": "missing markdown_path"}))
            return 1
        audio = None
        if "--audio" in sys.argv:
            i = sys.argv.index("--audio")
            audio = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        r = push_blog_post(sys.argv[2], audio_dir=audio)
    elif cmd == "pull":
        with _locked():
            ok = _pull()
        r = {"ok": ok}
    elif cmd == "ensure-lfs":
        r = ensure_gitattributes_lfs()
    else:
        print(json.dumps({"ok": False, "error": f"unknown command: {cmd}"}))
        return 1
    print(json.dumps(r, indent=2))
    return 0 if r.get("ok") else 2


if __name__ == "__main__":
    sys.exit(main())
