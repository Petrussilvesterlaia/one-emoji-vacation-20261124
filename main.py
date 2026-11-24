"""One Emoji, One Dream Vacation.

Writes exactly one emoji -- a palm tree -- to /output/entry.txt and
nothing else. The palm tree is the universal postcard of a tropical
escape: one glance and a stranger sees the beach, the sun, and the
flight it takes to get there.

Why this emoji: it is a single Unicode code point (U+1F334) with
default emoji presentation, so it renders as a full-colour emoji on
every screen with no variation selector, ZWJ sequence, or modifier
needed -- it reads instantly across cultures and at small size.
"""

import os
import unicodedata

EMOJI = "\U0001F334"  # U+1F334 PALM TREE
EXPECTED_NAME = "PALM TREE"
EXPECTED_UTF8 = b"\xf0\x9f\x8c\xb4"

# The grader reads /output/entry.txt; ENTRY_OUTPUT_PATH lets the same
# program be exercised locally without touching the graded path.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def validate_emoji(text: str) -> None:
    """Assert the entry is exactly one emoji character.

    Checks, in order: a string, exactly one code point, not
    whitespace, a symbol (category So) whose Unicode name is the
    expected one, and no variation selector / ZWJ / modifier hiding
    in the string (impossible at length 1, asserted explicitly so a
    future edit cannot silently widen the entry).
    """
    assert isinstance(text, str), "entry must be a string"
    assert len(text) == 1, f"entry must be exactly one character, got {len(text)}"
    assert not text.isspace(), "entry must not be whitespace"
    assert unicodedata.category(text) == "So", (
        f"entry must be a symbol, got category {unicodedata.category(text)}"
    )
    assert unicodedata.name(text) == EXPECTED_NAME, (
        f"entry must be {EXPECTED_NAME}, got {unicodedata.name(text)}"
    )
    assert ord(text) == 0x1F334, "entry must be U+1F334 PALM TREE"
    assert text.encode("utf-8") == EXPECTED_UTF8, "entry bytes are not U+1F334"


def main() -> None:
    validate_emoji(EMOJI)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" keeps the file byte-exact: one emoji, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == EXPECTED_UTF8, f"file bytes are not U+1F334: {raw!r}"
    back = raw.decode("utf-8")
    validate_emoji(back)
    assert back == EMOJI, "round-trip mismatch"
    print(f"{EMOJI}  U+{ord(EMOJI):04X} {unicodedata.name(EMOJI)}  "
          f"({len(raw)} bytes)")


if __name__ == "__main__":
    main()
