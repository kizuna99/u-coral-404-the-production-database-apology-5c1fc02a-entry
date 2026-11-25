# SPDX-License-Identifier: MIT
"""Write the winning one-line production-database apology to /output/entry.txt."""
import os

TEXT = "Sorry, I deleted the production database - then tried to log this apology in it, and that failure in it too. Third try, in person: hi, I'm the incident report."


def render():
    """Return the exact entry text (single line, 159 characters, gate-checked)."""
    assert 1 <= len(TEXT) <= 200 and TEXT.strip() and "\n" not in TEXT
    return TEXT


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render())
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(render())


if __name__ == "__main__":
    main()
