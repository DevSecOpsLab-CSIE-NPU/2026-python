import sys


def main() -> None:
	# True 代表下一個雙引號要替換成開引號 ``
	is_open_quote = True
	# 用串列累積字元，最後一次 join 輸出效率較佳
	output_parts = []

	# 讀取整份輸入，逐字處理
	for ch in sys.stdin.read():
		if ch == '"':
			# 交替替換：開引號 ``、閉引號 ''
			if is_open_quote:
				output_parts.append("``")
			else:
				output_parts.append("''")
			# 每遇到一個雙引號就切換狀態
			is_open_quote = not is_open_quote
		else:
			# 非雙引號字元原樣保留
			output_parts.append(ch)

	# 輸出轉換後結果
	sys.stdout.write("".join(output_parts))


if __name__ == "__main__":
	main()
