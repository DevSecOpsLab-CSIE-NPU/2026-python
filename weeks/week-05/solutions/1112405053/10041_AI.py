import sys


# 逐行讀到 EOF：每行都是一個十進位整數
for line in sys.stdin:
	n = int(line.strip())
	# bin(n) 會得到像 "0b101"，切掉前兩個字元後就是純二進位
	print(bin(n)[2:])