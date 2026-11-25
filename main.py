"""Entry for the make.fun bounty news-image-20261125.

The image beside this file (entry.png) sums up the world news of
Wednesday 25 November 2026. This program copies it to the output, the
way the kit's starter does: an explicit output path as the first
argument wins, then MAKEFUN_OUTPUT_DIR (which stands in for /output
outside the grader's container), then /output itself. No network, no
inputs: every run writes the same bytes.
"""

import os
import shutil
import sys
from pathlib import Path

src = Path(__file__).with_name("entry.png")
if len(sys.argv) > 1:
    target = Path(sys.argv[1])
    out_path = target if target.suffix else target / "entry.png"
else:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_path = out_dir / "entry.png"
out_path.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_path)
