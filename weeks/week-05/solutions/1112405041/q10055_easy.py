import sys

# 仲夏夜之夢（複合函數增減性）- 大一小萌新簡單版
# 這題是教授特別設計的釣魚題，如果你寫成物理相減就輸了。
# 💡 核心：增(0)與減(1)複合遵循 XOR 邏輯，奇數個減函數結果為減(1)。

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n, q = int(input_data[0]), int(input_data[1])
    status = [0] * (n + 1) # 一開始都是增(0)

    ptr = 2
    for _ in range(q):
        op = int(input_data[ptr]); ptr += 1
        if op == 1:
            i = int(input_data[ptr]); ptr += 1
            status[i] ^= 1 # 0變1, 1變0
        else:
            l, r = int(input_data[ptr]), int(input_data[ptr+1]); ptr += 2
            ans = 0
            for k in range(l, r + 1):
                ans ^= status[k]
            print(ans)

if __name__ == "__main__":
    main()
