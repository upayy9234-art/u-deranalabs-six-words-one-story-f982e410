"""Six Words, One Story — a make.fun program/v1 entry.

Writes one complete story, told in exactly six words, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), where the
harness's gate scorer and judge read it.

The story: "Dad's chair stays set. Every Christmas."
A father is gone, and the family still sets his place at the table,
every year. Six words carry the loss, the ritual that refuses to let
it end, and all the Christmases in between — the rest is the reader's
to fill in.
"""

import os

STORY = "Dad's chair stays set. Every Christmas."


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
