
import sys
import re
import random


def generate_numbers(y: int):
	"""Generate a deterministic sequence of y numbers.

	The sequence uses y as the random seed so the same input always
	produces the same output, which keeps the result reproducible.
	"""
	rng = random.Random(y)
	upper_bound = max(10, y * 2)
	return [rng.randint(1, upper_bound) for _ in range(y)]


def process_input(text: str):
	text = text.strip()
	if not text:
		return None
	try:
		y = int(text)
	except ValueError:
		print("請輸入整數")
		return None
	if y <= 0:
		print("請輸入正整數")
		return None

	nums = generate_numbers(y)
	print(f"目前數列：{' '.join(map(str, nums))}")

	# remove duplicates while keeping original order
	seen = set()
	unique = []
	for n in nums:
		if n not in seen:
			seen.add(n)
			unique.append(n)

	# keep numbers divisible by 5 and sort ascending
	result = sorted(n for n in unique if n % 5 == 0)
	return result


def main():
	data = sys.stdin.read()
	if not data:
		return
	res = process_input(data)
	if res is None:
		return
	if res:
		print(' '.join(map(str, res)))
	else:
		print("NONE")


if __name__ == '__main__':
	main()
