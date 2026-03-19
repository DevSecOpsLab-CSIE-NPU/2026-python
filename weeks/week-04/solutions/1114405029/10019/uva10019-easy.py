def solve(data: str) -> str:
    # 先把整份輸入依照換行切開，並去掉前後多餘空白
    lines = data.strip().splitlines()

    # 第一行表示總共有幾組測試資料
    t = int(lines[0])

    # 用來儲存每組測資的答案
    result_lines = []

    # 逐組處理
    for i in range(1, t + 1):
        # 讀入這一組數字，先用字串保留原始形式
        s = lines[i].strip()

        # b1：
        # 把字串 s 當成十進位整數
        decimal_value = int(s)

        # 把十進位整數轉成二進位字串，再計算其中有幾個 '1'
        b1 = bin(decimal_value).count("1")

        # b2：
        # 把字串 s 當成十六進位數字
        # 例如 "265" 代表十六進位 265，不是十進位 265
        hex_value = int(s, 16)

        # 再轉成二進位，計算其中有幾個 '1'
        b2 = bin(hex_value).count("1")

        # 按題目要求輸出 b1 和 b2，中間用空白隔開
        result_lines.append(f"{b1} {b2}")

    # 每組答案以換行連接
    return "\n".join(result_lines)


if __name__ == "__main__":
    import sys

    # 從標準輸入讀取資料，交給 solve 處理後輸出
    input_data = sys.stdin.read()
    print(solve(input_data))