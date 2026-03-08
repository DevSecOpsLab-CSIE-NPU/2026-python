from typing import Iterable, List, Tuple


def sort_students(records: Iterable[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
	"""回傳排序後的學生清單。

	使用 `sorted(..., key=...)` 指定排序鍵：
	- 以 score 降冪（使用負值實作）
	- age 升冪
	- name 升冪（字母序）
	"""
	return sorted(records, key=lambda r: (-int(r[1]), int(r[2]), r[0]))


if __name__ == "__main__":	
	students = [
		("Alice", 88, 20),
		("Bob", 95, 22),
		("Charlie", 88, 19),
		("David", 95, 21),
		("Eve", 88, 20),
		("Frank", 70, 23),
		("Grace", 88, 19),
		("Heidi", 95, 22),
		("Ivan", 70, 22),
	]

	ranked = sort_students(students)

	# 互動輸入：兩個整數 N K
	# - N 表示要查看第 N 名（以 1 為起始）
	# - K 表示從第 N 名開始往下要顯示多少名
	# 若直接按 Enter 則列印全部排名
	try:
		s = input('請輸入兩個整數 N K（以空白分隔，直接 Enter 列印全部）：').strip()
	except EOFError:
		s = ''

	if not s:
		for name, score, age in ranked:
			print(f"{name} {score} {age}")
	else:
		parts = s.split()
		if len(parts) < 2:
			print('輸入錯誤：請提供兩個整數 N K（例如: 2 3）')
		else:
			try:
				n = int(parts[0])
				k = int(parts[1])
			except ValueError:
				print('輸入必須為整數')
			else:
				if n <= 0 or k <= 0:
					print('N 與 K 必須為大於 0 的整數')
				else:
					start = n - 1
					end = start + k
					if start >= len(ranked):
						print(f'N={n} 超出範圍（總人數 {len(ranked)}）')
					else:
						print(f'顯示第 {n} 名起，共 {k} 名（如有不足則顯示到最後一名）:')
						for name, score, age in ranked[start:end]:
							print(f"{name} {score} {age}")
