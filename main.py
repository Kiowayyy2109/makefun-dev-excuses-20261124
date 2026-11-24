#!/usr/bin/env python3
"""Developer Excuses — one line, deterministic.

The excuse every developer has either said or swallowed: the code was
never broken, the environment was. Prints exactly one line under 200
characters and nothing else.
"""

LINE = (
    "It worked on my machine, so we shipped my machine. "
    "Production is now my laptop, and my laptop is asleep."
)


def validate_line(text):
    """The brief allows exactly one line of 1-200 characters."""
    assert "\n" not in text, "must be a single line"
    assert 1 <= len(text) <= 200, "must be 1-200 characters"
    return text


def main():
    print(validate_line(LINE))


if __name__ == "__main__":
    main()
