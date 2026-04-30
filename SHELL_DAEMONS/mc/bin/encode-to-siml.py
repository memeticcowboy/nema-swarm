#!/usr/bin/env python3
"""
encode-to-siml.py — thin wrapper that delegates to nema_harness/skills/simlab/encode.sh.

[REBUILT 2026-04-28 from session reference. The original was lost in MC's
 destructive "pause Daily Encounters" cleanup. encode.sh sources secrets +
 routes to either the simlab daemon (port 8820), kimi direct subprocess,
 or the python orchestrator depending on --mode.]

Usage: same args as encode.sh. Pass-through wrapper.

  encode-to-siml.py --source-url https://example.com/concept --series E
  encode-to-siml.py --source-text "..." --series Z --name-hint Consider
  encode-to-siml.py --mode python --source-file /tmp/essay.pdf
"""

import os
import subprocess
import sys

HARNESS_ENCODE = "/Users/nema/Projects/nema_harness/skills/simlab/encode.sh"


def main() -> int:
    if not os.path.isfile(HARNESS_ENCODE):
        print(f'{{"ok": false, "error": "harness skill missing at {HARNESS_ENCODE}"}}')
        return 1
    # Pass all args through; encode.sh sources secrets + execs orchestrator.py
    return subprocess.call(["/bin/bash", HARNESS_ENCODE, *sys.argv[1:]])


if __name__ == "__main__":
    sys.exit(main())
