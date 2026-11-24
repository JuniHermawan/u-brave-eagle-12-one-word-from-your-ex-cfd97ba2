#!/usr/bin/env python3
"""One Word From Your Ex -- writes one word to /output/entry.txt.

Competition: u-brave-eagle-12-one-word-from-your-ex-cfd97ba2 (make.fun).
Gate: /output/entry.txt must be UTF-8 text of 1-24 characters, not only
whitespace. The word below is exactly one word, 8 chars, no newline.

Word: practice -- the word an ex would use to describe you: you were
practice. The rehearsal before the real thing. Painfully true, and the
entrant plainly knows it.
Proxy 24/25, rubric 24/25 (v2 pick; see proxy.py in the work dir).
Judge criteria in order: exactly one word an ex might use to describe you;
laugh out loud through surprise or a sharp turn; stings with recognition,
painfully true; lands instantly, no explanation, irreplaceable by a near
synonym; relatable, the kind of word people repeat because they have lived
it too.

Version history:
  v1 (24 Nov ~20:30 WIB): minimal writer; 95 candidates + 2 controls.
      Top tie practice/placeholder/footnote, proxy 24, rubric 24. v1 proxy
      gaps: dumpsterfire c4 3 vs 4, sloth/runaway/puppy/passenger/outdated/
      expired/storm/cat/mirror/virus/shadow c5 4 vs 5, vintage c3 4 vs 3,
      culdesac c2 4 vs 3, standin c4 3 vs 4.
  v2 (24 Nov ~20:35 WIB): dumpsterfire/standin into FRESH4, vintage/mirror
      into STING3, culdesac into LAUGH3, runaway out of FRESH4/NICHE4, the
      plain common words out of NICHE4. Every row now matches the hand
      rubric exactly. Top tie stands: practice/placeholder/footnote 24/24.
  v2 FREEZE: tie-break -- placeholder (11 chars) drops on size; practice
      and footnote tie at 8 chars, and practice leads on c3 (stings with
      recognition, 5 vs 4), the higher-weighted criterion. Pick: practice.
      Runners-up typo/sidequest/layover/beta/appendix at 23, dumpsterfire
      at 23.
"""
import os
import sys
from pathlib import Path

WORD = "practice"


def _gate_ok(word):
    """Mirror of the house gate: 1-24 chars, UTF-8, not only whitespace,
    exactly one word."""
    return (
        1 <= len(word) <= 24
        and word.strip() == word
        and word
        and len(word.split()) == 1
        and word.isascii()
    )


def main():
    if not _gate_ok(WORD):
        print(f"gate failed for word: {WORD!r}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(WORD, encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
