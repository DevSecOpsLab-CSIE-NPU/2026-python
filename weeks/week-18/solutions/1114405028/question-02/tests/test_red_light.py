import subprocess
import sys
from pathlib import Path


def test_red_light_parse_shift_line():
    solver_path = Path(__file__).resolve().parents[1] / "solver.py"
    proc = subprocess.run(
        [sys.executable, str(solver_path)],
        input="Hello, NPU!\n9\n",
        text=True,
        capture_output=True,
    )
    assert proc.returncode == 0
    assert proc.stdout.strip() == "Qnuux, WYD!"
