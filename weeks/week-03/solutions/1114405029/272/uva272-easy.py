import sys

# 記錄現在是不是在引號內
inside = False

# 一行一行讀取輸入
for line in sys.stdin:

    result = ""

    # 檢查每個字元
    for ch in line:

        # 如果遇到 "
        if ch == '"':

            # 如果目前不在引號內，代表是開引號
            if inside == False:
                result += "``"
            else:
                # 否則是關引號
                result += "''"

            # 切換狀態
            inside = not inside

        else:
            result += ch

    # 輸出結果
    print(result, end="")