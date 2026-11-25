"""Write one funny line to /output/entry.txt.

The line is a hopeless tech support agent's reply to a desperate
customer, for make.fun's "Have You Tried Turning It Off?" bounty.
The program is deterministic: it always writes the same bytes,
uses no network, and depends on nothing outside this repository.
"""

import os

TEXT = (
    "Sir, I turned it off and on again and now it's asking me for "
    "tech support, so if you could hold \u2014 I'm going to put us "
    "both on hold with each other."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate requires 1 to 199 characters; fail loudly instead of
# ever writing an entry the judge will never see.
assert 1 <= len(TEXT) <= 199, "entry text outside the 1-199 gate"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
