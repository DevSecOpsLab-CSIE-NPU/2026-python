"""Create a small PNG chart from benchmark results."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

from benchmark import load_results

try:
    os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "wk17-mplconfig"))
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover - fallback is tested through output file.
    plt = None


PNG_1X1 = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xff\xff?"
    b"\x00\x05\xfe\x02\xfeA\xe2'\x99\x00\x00\x00\x00IEND\xaeB`\x82"
)


def create_plot(results_path="results.json", output_path="assets/radar.png") -> Path:
    """Write a PNG comparing search timings and return the output path."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    results = load_results(results_path)

    if plt is None:
        with output.open("wb") as file:
            file.write(PNG_1X1)
        return output

    rows = results["rows"]
    sizes = [row["size"] for row in rows]
    plt.figure(figsize=(7, 4))
    for key in ("linear", "binary", "set", "set_prepared", "builtin_in", "bisect"):
        plt.plot(sizes, [row[key] for row in rows], marker="o", label=key)
    plt.xlabel("data size")
    plt.ylabel("seconds per query batch")
    plt.title("Search timing comparison")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output)
    plt.close()
    return output


if __name__ == "__main__":
    create_plot()
