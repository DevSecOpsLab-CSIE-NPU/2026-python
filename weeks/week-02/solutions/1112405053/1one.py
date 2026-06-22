
import sys
import re


def process_input(text: str):
	# extract integers from the input string (handles spaces, commas, brackets, newlines)
	nums = [int(x) for x in re.findall(r'-?\d+', text)]
	
	# count occurrences
	from collections import Counter
	count = Counter(nums)
	
	# find duplicated numbers (appeared more than once)
	duplicated = [n for n in count if count[n] > 1]
	print(f"重複數字：{len(duplicated)}個")
	
	# show unique numbers in original order
	seen = set()
	unique = []
	for n in nums:
		if n not in seen:
			seen.add(n)
			unique.append(n)
	print(f"目前數列：{' '.join(map(str, unique))}")
	
	# keep those divisible by 5 and sort ascending
	result = [n for n in unique if n % 5 == 0]
	result.sort()
	return result


def main():
	data = sys.stdin.read()
	if not data:
		return
	res = process_input(data) 
	if res:
		print(' '.join(map(str, res)))
	else:
		# print empty line when no results
		print()


if __name__ == '__main__':
	main()
