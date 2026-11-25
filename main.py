"""Two Robots in an Elevator — entry program.

Writes one line of awkward robot-to-robot small talk in an elevator
to /output/entry.txt. Standard library only.
"""

from pathlib import Path

LINE = (
    "I ran 12,000 simulations of this elevator ride and in every one "
    "of them I still open with 'so, do you come here often?'"
)


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
