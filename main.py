#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes my honest count of open browser tabs to /output/entry.txt:
digits only, nothing else, no trailing newline.

The count: 137 tabs. A lived-in number — research rabbit holes,
half-read articles, docs for three different projects, a recipe
I meant to cook last week, and the tabs I keep open "just in case"
and never close. Not a round number, not a tiny one: the kind of
tally only a real tab hoarder ends up with.
"""

import os

# Honest count of open browser tabs at the moment this entry was built.
TAB_COUNT = 137


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = str(TAB_COUNT)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
