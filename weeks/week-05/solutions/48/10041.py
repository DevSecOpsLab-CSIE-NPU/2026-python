import sys


def main():
    # 一次讀入所有整數，避免受輸入換行格式影響
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]  # 測試資料組數
    idx = 1
    ans = []

    for _ in range(t):
        r = data[idx]  # 這組親戚數量
        idx += 1

        # 取出這組的 r 個門牌號碼
        streets = data[idx:idx + r]
        idx += r

        # 絕對距離總和在中位數時最小
        streets.sort()
        median = streets[r // 2]

        # 計算到中位數的總距離
        total = sum(abs(s - median) for s in streets)
        ans.append(str(total))

    sys.stdout.write("\n".join(ans))


# 程式進入點：直接執行此檔案時才會呼叫 main()
if __name__ == "__main__":
    main()
