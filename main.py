"""One-Line Roast: The Gadget You Use Every Day entry.

Writes one original roast to /output/entry.txt, aimed at a gadget used
every day in this household: the microwave, and its habit of beeping
long after the food is ready.
"""

import os

ENTRY = (
    "My microwave beeps five times when my food is ready, then beeps "
    "again every minute, as if I'll forget the meal I was standing "
    "right in front of."
)


def main():
    # Gate in the kit: 1 to 200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
