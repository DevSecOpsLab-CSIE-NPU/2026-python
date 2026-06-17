"""
Run unittest for UVA 12019 and save a UTF-8 log file.
"""

import subprocess
import sys


result = subprocess.run(
    [sys.executable, "weeks/week-14/solutions/1114405022/test_12019_doomsday.py"],
    capture_output=True,
    text=True,
)

with open("weeks/week-14/solutions/1114405022/test_log_12019.txt", "w", encoding="utf-8") as file:
    file.write(result.stdout)
    file.write(result.stderr)

sys.exit(result.returncode)
