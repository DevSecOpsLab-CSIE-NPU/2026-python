import sys


def main() -> None:
	# 一次讀入所有輸入文字（包含換行）
	text = sys.stdin.read()
	# True 代表下一個雙引號要轉成左引號 ``，False 轉成右引號 ''
	is_open = True
	output = []

	# 逐字處理：遇到 " 就依序替換，其他字元原樣保留
	for char in text:
		if char == '"':
			if is_open:
				output.append("``")
			else:
				output.append("''")
			is_open = not is_open
		else:
			output.append(char)

	# 輸出轉換後完整結果
	sys.stdout.write("".join(output))


if __name__ == "__main__":
	main()
