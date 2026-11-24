"""One-Liner Laugh Lab (make.fun bounty u-suroso-69-one-liner-laugh-lab-6ccf3aae).

Writes a single funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Deterministic, no network, no
randomness, no input: the same line, byte for byte, on every run.
The line was chosen for the judge's brief: a real surprise at the end
(the sock was adopted, not eaten, and is now thriving under the couch)
that still makes sense, an everyday truth everyone recognises (a
vacuum eating a sock), and economy of words - 91 characters, two short
sentences, nothing left to explain.
"""

import os

LINE = (
    "I didn't eat your sock; I adopted it. "
    "It lives under the couch and, frankly, it's thriving."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. This line is 91 characters.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
