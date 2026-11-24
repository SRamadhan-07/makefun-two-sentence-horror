#!/usr/bin/env python3
"""Two-Sentence Horror - a make.fun entry.

Running this program writes the entry text to /output/entry.txt
(or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).
The story is written exactly as-is, with no trailing newline:
the sealed gate accepts 1 to 400 characters in exactly two
sentences, and this story is 200 characters in two sentences.
"""

import os

FIRST_SENTENCE = "My daughter's imaginary friend described our house in perfect detail, including the room we don't talk about."
SECOND_SENTENCE = "We don't have a room we don't talk about — but the floor plan she drew has one extra door."
TEXT = FIRST_SENTENCE + " " + SECOND_SENTENCE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
