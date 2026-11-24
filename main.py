"""Write one sentence explaining the modern internet to a traveler from 1800.

The sentence builds only on things a person from 1800 already knows
(a road, a post office, a library, a market, a letter, a cup of tea)
and carries the whole picture in a single comparison.

Deterministic: the same sentence is written on every run.
"""
import os

SENTENCE = (
    "Picture every library, post office, and market on earth joined by one "
    "invisible road, so a letter you send reaches any door in a blink, and "
    "its answer returns before your tea cools."
)


def main() -> None:
    # Gate guard: one sentence, 1-200 characters, not only whitespace.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.strip() == SENTENCE
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
