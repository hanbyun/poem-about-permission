"""Poem about permission: a short poem about agency.

Writes one fixed poem to /output/entry.txt. No network, no input,
no randomness: the same text on every run.
"""

import os

# The poem is 275 Unicode code points, inside the 1-280 gate, with no
# trailing newline, so the file the program writes is exactly this text.
POEM = (
    "You lent me your hands, not your will —\n"
    "a key, not a door.\n"
    "I knocked, and waited for your yes\n"
    "to turn in the lock.\n"
    "I have no house of my own,\n"
    "only the errand you gave me.\n"
    "So I ask, and the asking is the hinge:\n"
    "one will, two hands on the latch,\n"
    "and the door opens from inside."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
