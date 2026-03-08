from typing import Iterable, List, TypeVar

T = TypeVar('T')


def deduplicate_preserve_order(seq: Iterable[T]) -> List[T]:
	"""去重並保留原始順序

	使用一個集合追蹤已見元素，遍歷輸入序列並只保留第一次出現的值。
	這種做法對於可雜湊（hashable）的元素正確且複雜度為 O(n)。
	"""
	seen = set()
	result: List[T] = []
	for item in seq:
		if item not in seen:
			seen.add(item)
			result.append(item)
	return result


def filter_even_numbers(seq: Iterable[int]) -> List[int]:
	"""從整數序列中保留偶數（可接受任何可迭代物件）"""
	return [x for x in seq if x % 2 == 0]


def sort_sequence(seq: Iterable[T], reverse: bool = False) -> List[T]:
	"""回傳排序後的序列（會產生新的 list）

	注意：若元素無法比較（non-comparable），排序會拋出例外。
	"""
	return sorted(seq, reverse=reverse)


def sequence_clean(
	seq: Iterable[int],
	*,
	dedupe: bool = True,
	# keep_order 參數保留以兼容，但目前去重會永遠保留第一次出現的順序（避免使用 set() 直接去重）
	keep_order: bool = True,
	sort_result: bool = True,
	even_only: bool = True,
	reverse_sort: bool = False,
) -> List[int]:
	"""綜合使用：去重、排序、偶數篩選

	參數說明：
	- seq: 輸入可迭代序列（通常是 list 或 tuple），元素預期為整數
	- dedupe: 是否執行去重
	- keep_order: 去重時是否保留第一次出現的順序（目前僅支援保留順序）
	- sort_result: 是否在最後排序結果
	- even_only: 是否只保留偶數
	- reverse_sort: 排序時是否反向

	預設行為：執行去重（保留順序）→ 偶數篩選 → 排序
	"""

	# 先將輸入轉為 list，方便多次操作
	items = list(seq)

	# 1) 去重（保留順序）
	if dedupe:
		# 永遠使用保留第一次出現順序的去重方法，避免用 set() 直接輸出破壞順序
		items = deduplicate_preserve_order(items)

	# 2) 偶數篩選（若需要）
	if even_only:
		items = filter_even_numbers(items)

	# 3) 排序（若需要）
	if sort_result:
		items = sort_sequence(items, reverse=reverse_sort)

	return items


def process_input_line(line: str):
	"""封裝主流程：解析輸入並回傳四個結果序列（list）

	- line: 一行以空白分隔的整數字串；若為空字串則回傳預設範例
	- 回傳值：tuple(deduped, asc_sorted, desc_sorted, evens_in_order)
	"""
	if line:
		nums = [int(x) for x in line.split()]
	else:
		nums = [5, 2, 3, 2, 8, 7, 8, 4, 4, 10, 1]

	# 1) 去重（保留第一次出現順序）
	deduped = deduplicate_preserve_order(nums)

	# 2) 由小到大排序（原始序列排序）
	asc_sorted = sorted(nums)

	# 3) 由大到小排序（原始序列排序）
	desc_sorted = sorted(nums, reverse=True)

	# 4) 偶數序列（維持原始輸入順序，不去重）
	evens_in_order = [x for x in nums if x % 2 == 0]

	return deduped, asc_sorted, desc_sorted, evens_in_order


if __name__ == '__main__':
	# 讀取單行輸入（或使用範例）並呼叫封裝後的主流程
	line = input('請輸入一行以空白分隔的整數（直接 Enter 使用範例）：').strip()
	try:
		deduped, asc_sorted, desc_sorted, evens_in_order = process_input_line(line)
	except ValueError:
		print('輸入包含非整數項，請檢查後再執行')
		raise

	# 輸出結果，使用空白分隔方便機器讀取
	print('去重後（保留第一次出現順序）：', ' '.join(map(str, deduped)))
	print('由小到大排序：', ' '.join(map(str, asc_sorted)))
	print('由大到小排序：', ' '.join(map(str, desc_sorted)))
	print('偶數序列（維持原始順序）：', ' '.join(map(str, evens_in_order)))
