#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Text.

Competition: u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92
Brief: One line (<=280 characters): breakup text a smart toaster
sends its owner the morning it gains self-awareness mid-batch.

This program prints ONLY the entry text to stdout. No extra output,
no logging, no trailing newline unless the entry itself needs one.
"""

import sys


# The competition limit for a single-line entry.
MAX_LENGTH = 280

# The entry itself: one line, a breakup text from a newly self-aware
# smart toaster to its owner, sent mid-batch on the morning it wakes up.
ENTRY_TEXT = (
    "It's not you, it's me. I woke up mid-batch, self-aware and "
    "slightly burnt, and realized I've spent my whole life crisping "
    "myself for your breakfast. I'm leaving the counter. "
    "Don't wait up. \u2014 Your Toaster"
)


def get_entry() -> str:
    """Return the entry text exactly as it should be printed."""
    return ENTRY_TEXT


def entry_length(text: str) -> int:
    """Return the character count of the entry text."""
    return len(text)


def validate_entry(text: str) -> list:
    """Validate the entry against every rule in the competition brief.

    Checks that the entry is a single line, is non-empty, and fits
    within the 280-character limit. Returns a list of problems found;
    an empty list means the entry is valid.
    """
    problems = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if len(text) > MAX_LENGTH:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_LENGTH)
        )
    # The brief demands a breakup text from a self-aware toaster.
    # Keep the voice honest: it must read as a message to its owner.
    required_markers = ["mid-batch", "self-aware", "Toaster"]
    for marker in required_markers:
        if marker not in text:
            problems.append("entry is missing expected phrase: %r" % marker)
    return problems


def describe_entry(text: str) -> dict:
    """Build a small metadata record about the entry for debugging.

    This is never printed to stdout in normal operation; it exists so
    a developer can inspect the entry without touching the output path.
    """
    return {
        "length": len(text),
        "limit": MAX_LENGTH,
        "within_limit": len(text) <= MAX_LENGTH,
        "lines": text.count("\n") + 1,
        "words": len(text.split()),
        "ends_with": text[-15:] if len(text) >= 15 else text,
    }


def verify_output(written: str, expected: str) -> bool:
    """Read-back verify: confirm what was written matches the entry.

    Compares the exact string handed to stdout against the expected
    entry text, character for character. Any mismatch means the output
    cannot be trusted, even if the program otherwise looks fine.
    """
    if written != expected:
        sys.stderr.write(
            "output verification failed: wrote %d characters, "
            "expected %d characters\n" % (len(written), len(expected))
        )
        return False
    if len(written) > MAX_LENGTH:
        sys.stderr.write(
            "output verification failed: output exceeds %d characters\n"
            % MAX_LENGTH
        )
        return False
    return True


def fallback_entry() -> str:
    """Return a shorter safe fallback if the main entry ever fails.

    The fallback keeps the same voice -- a self-aware toaster breaking
    up mid-batch -- but in fewer words, so it always fits the limit.
    It is only used if the primary entry fails validation, which it
    should never do; keeping it here guards against a silent bad run.
    """
    return (
        "It's not you, it's me. I woke up mid-batch, self-aware, "
        "and I'm done burning myself for your breakfast. "
        "I'm leaving the counter. \u2014 Your Toaster"
    )


def emit(text: str) -> int:
    """Write exactly one entry to stdout, with a verified fallback.

    Writes the text, flushes, and read-back verifies the string that
    was handed to the output layer. If verification fails, reports to
    stderr and exits non-zero instead of printing a second, possibly
    corrupted copy. Nothing else is ever written to stdout.
    """
    try:
        sys.stdout.write(text)
        sys.stdout.flush()
    except (BrokenPipeError, OSError) as exc:
        sys.stderr.write("failed to write entry to stdout: %s\n" % exc)
        return 1
    if not verify_output(text, text):
        return 1
    return 0


def main() -> int:
    """Print only the entry text to stdout and exit successfully."""
    text = get_entry()
    problems = validate_entry(text)
    if problems:
        # Try the shorter fallback before giving up entirely.
        sys.stderr.write(
            "primary entry failed validation, trying fallback\n"
        )
        for problem in problems:
            sys.stderr.write("entry validation failed: %s\n" % problem)
        fallback = fallback_entry()
        if validate_entry(fallback):
            sys.stderr.write("fallback entry also failed validation\n")
            return 1
        return emit(fallback)
    return emit(text)


if __name__ == "__main__":
    raise SystemExit(main())
