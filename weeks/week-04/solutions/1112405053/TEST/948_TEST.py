import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


DEFAULT_INPUT = """2

5 3
2 1 2 3 4
<
1 1 4
=
1 2 5
=

4 2
1 1 2
<
1 3 4
=
"""


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument("--runs", type=int, default=5)
	parser.add_argument("--input", type=str, default="")
	args = parser.parse_args()

	test_dir = Path(__file__).resolve().parent
	target_script = test_dir.parent / "948_ME.py"
	result_json = test_dir / "948_test_results.json"
	result_txt = test_dir / "948_test_results.txt"

	if args.input:
		input_data = Path(args.input).read_text(encoding="utf-8")
	else:
		input_data = DEFAULT_INPUT

	all_results = []

	for run_index in range(1, args.runs + 1):
		start = time.perf_counter()
		completed = subprocess.run(
			[sys.executable, str(target_script)],
			input=input_data,
			text=True,
			capture_output=True,
		)
		elapsed_ms = round((time.perf_counter() - start) * 1000, 3)

		record = {
			"run": run_index,
			"timestamp": datetime.now().isoformat(timespec="seconds"),
			"exit_code": completed.returncode,
			"elapsed_ms": elapsed_ms,
			"stdout": completed.stdout,
			"stderr": completed.stderr,
		}
		all_results.append(record)

	result_json.write_text(
		json.dumps(all_results, ensure_ascii=False, indent=2),
		encoding="utf-8",
	)

	lines = []
	for record in all_results:
		lines.append(f"Run #{record['run']}")
		lines.append(f"timestamp: {record['timestamp']}")
		lines.append(f"exit_code: {record['exit_code']}")
		lines.append(f"elapsed_ms: {record['elapsed_ms']}")
		lines.append("stdout:")
		lines.append(record["stdout"].rstrip("\n"))
		lines.append("stderr:")
		lines.append(record["stderr"].rstrip("\n"))
		lines.append("-" * 40)

	result_txt.write_text("\n".join(lines) + "\n", encoding="utf-8")

	print(f"Done. Ran {args.runs} times.")
	print(f"JSON: {result_json}")
	print(f"TXT : {result_txt}")


if __name__ == "__main__":
	main()
