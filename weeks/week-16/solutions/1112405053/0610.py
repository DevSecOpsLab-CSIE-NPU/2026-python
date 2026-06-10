#!/usr/bin/env python3
"""
ZeroJudge c813 / UVA 11332 - Summing Digits

Read integers (one per line) until a line containing 0. For each n != 0,
print g(n) where g(n) is the repeated digit-sum until a single digit remains.

This file implements the solution in-place as requested. 
"""

import sys


def digital_root_from_str(s: str) -> str:
	"""Return the digital root as a string for the non-zero numeric string s."""
	# Fast path: use modulo only when number fits in integer; but s length is small here.
	# Simpler and safe approach: repeatedly sum digits until single digit.
	while len(s) > 1:
		total = 0
		for ch in s:
			if '0' <= ch <= '9':
				total += ord(ch) - 48
		s = str(total)
	return s


def main():
	out_lines = []
	for line in sys.stdin:
		token = line.strip()
		if not token:
			continue
		if token == '0':
			break
		out_lines.append(digital_root_from_str(token))
	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()

