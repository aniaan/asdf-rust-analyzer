import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from lib.lib import Plugin

PLUGIN = Plugin(
    name="rust-analyzer",
    cmd="rust-analyzer",
    repo_name="rust-lang/rust-analyzer",
    filename_template="rust-analyzer-{arch}-{platform}.gz",
    platform_map={
        "darwin": "apple-darwin",
        "linux": "unknown-linux-gnu",
    },
    bin_path="rust-analyzer",
)
