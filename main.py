"""Hand the finished front page to the runner, byte for byte.

The artwork is already complete inside entry.png, which sits in this same
folder. This script does no drawing and no editing at all: it simply puts an
exact copy of that image where the harness expects it, so every run of the
entry hands over identical bytes.
"""

import os, shutil, sys


def _pick_target(argv):
    """Decide the full output file path from the CLI and the environment."""
    folder = os.path.dirname(os.path.abspath(__file__))
    picture = os.path.join(folder, "entry.png")
    if len(argv) > 1:
        chosen = argv[1]
        if os.path.isdir(chosen):
            chosen = os.path.join(chosen, "entry.png")
        return picture, chosen
    root = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return picture, os.path.join(root, "entry.png")


def main(argv):
    picture, chosen = _pick_target(argv)
    if os.path.abspath(chosen) == os.path.abspath(picture):
        print("entry.png is already in place; nothing to copy.")
        return 0
    parent = os.path.dirname(chosen)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(picture, chosen)
    print("wrote " + chosen)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
