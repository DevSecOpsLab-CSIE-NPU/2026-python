# 題目 10101

**題名**: UVA 10101

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a094)
- [Yui Huang 題解](https://yuihuang.com/zj-a094/)

## 題目敘述

這是一個很古老的遊戲：用**木棒**在桌上拼出一個**不成立的等式**，移動且只移動**一根木棒**使得等式成立。

現在輪到你了：從輸入讀入一個式子，如果移動一根木棒可以使等式成立，則輸出新的等式，否則輸出 `No`。

**說明與限制：**

1. 式子中只會出現**加號和減號**（包括負號），且有且僅有一個等號。不會出現括號、乘號或除號，也不會有 `++`、`--`、`+-` 或 `-+` 出現。
2. 式子中不會出現 **8 個或 8 個以上的連續數字**。
3. 你只能移動用來構成**數字的木棒**，不能移動構成運算符（`+`、`-`、`=`）的木棒，所以加號、減號、等號不會改變。移動前後，木棒構成的數字必須嚴格符合標準七段顯示器的 0~9。
4. 修改**前**的等式中的數不會以 `0` 開頭，但允許修改**後**的等式中的數以數字 `0` 開頭。

## 輸入說明

從輸入讀入一行字串，該字串包括一個以 **`#`** 字元結尾的式子（ASCII 碼 35）。

- 式子中沒有空格或其他分隔符
- 輸入資料嚴格符合邏輯
- 字串長度 ≤ 1000
- 注意：`#` 字元後面可能有一些與題目無關的字元

## 輸出說明

輸出僅一行：

- 若**有解**，輸出正確的等式，格式與輸入格式相同（以 `#` 結尾，中間不能有分隔符，也不要加入多餘字元）。
- 若**無解**，輸出 `No`（N 大寫，o 小寫）。

---

## 解題思路

這題的關鍵是「只移動一根木棒，而且只能動到數字本身」。

做法如下：

1. 先把輸入字串切成「左式」與「右式」，只保留 `#` 以前的內容。
2. 找出所有數字的位置，記錄每個數字字元在字串中的索引。
3. 針對每一個數字位置，嘗試拿掉一根線段，並把這根線段加到另一個數字位置。
4. 兩個數字都改完後，檢查新的式子是否成立。
5. 只要找到第一個合法解就輸出，若全部都不行就輸出 `No`。

因為七段顯示器每個數字的可能變化數量很少，所以這個暴力搜尋在實作上是可行的。

## 解題代碼

```python
import sys


SEGMENTS = {
	"0": 0b1111110,
	"1": 0b0110000,
	"2": 0b1101101,
	"3": 0b1111001,
	"4": 0b0110011,
	"5": 0b1011011,
	"6": 0b1011111,
	"7": 0b1110000,
	"8": 0b1111111,
	"9": 0b1111011,
}


def parse_side(expr: str) -> int:
	total = 0
	number = ""
	sign = 1

	for index, char in enumerate(expr):
		if char in "+-":
			if index == 0 or expr[index - 1] in "+-=" or number == "":
				sign = -1 if char == "-" else 1
			else:
				total += sign * int(number)
				number = ""
				sign = -1 if char == "-" else 1
		else:
			number += char

	if number:
		total += sign * int(number)

	return total


def build_candidates():
	remove_map = {digit: [] for digit in SEGMENTS}
	add_map = {digit: [] for digit in SEGMENTS}

	for digit, mask in SEGMENTS.items():
		for other_digit, other_mask in SEGMENTS.items():
			if mask.bit_count() - other_mask.bit_count() == 1 and (other_mask & mask) == other_mask:
				remove_map[digit].append(other_digit)
			if other_mask.bit_count() - mask.bit_count() == 1 and (mask & other_mask) == mask:
				add_map[digit].append(other_digit)

	return remove_map, add_map


REMOVE_MAP, ADD_MAP = build_candidates()


def is_valid_equation(expr: str) -> bool:
	left, right = expr.split("=")
	return parse_side(left) == parse_side(right)


def main() -> None:
	raw = sys.stdin.read()
	if not raw:
		return

	expr = raw.split("#", 1)[0]
	chars = list(expr)
	digit_positions = [index for index, ch in enumerate(chars) if ch.isdigit()]

	for source_index in digit_positions:
		source_digit = chars[source_index]
		for removed_digit in REMOVE_MAP[source_digit]:
			chars[source_index] = removed_digit

			for target_index in digit_positions:
				if target_index == source_index:
					continue

				target_digit = chars[target_index]
				for added_digit in ADD_MAP[target_digit]:
					chars[target_index] = added_digit
					candidate = "".join(chars)
					if is_valid_equation(candidate):
						sys.stdout.write(candidate + "#")
						return
					chars[target_index] = target_digit

			chars[source_index] = source_digit

	sys.stdout.write("No")


if __name__ == "__main__":
	main()
```

## 測試用例

輸入：

```text
1+2=4#
```

輸出：

```text
1+2=3#
```
