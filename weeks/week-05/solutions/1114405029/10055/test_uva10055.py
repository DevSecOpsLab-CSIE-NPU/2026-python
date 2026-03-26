"""
UVA 10055 - Hashmat the Brave Warrior
測試程式版本

用途說明：
這份程式主要用來做本地測試。
程式將核心計算邏輯獨立成函式，
方便檢查答案是否正確，也方便後續維護與除錯。
"""


def calculate_difference(first_army, second_army):
    """
    計算兩支軍隊士兵數量的差距。

    參數：
        first_army (int)：第一支軍隊士兵數量
        second_army (int)：第二支軍隊士兵數量

    回傳：
        int：兩數差距的絕對值

    解題觀念：
        本題只需要輸出兩個整數的絕對差，
        也就是 abs(first_army - second_army)。
    """

    # 直接回傳兩數差距的絕對值
    return abs(first_army - second_army)


def solve():
    """
    依照 UVA 題目的輸入格式讀取資料並輸出答案。

    注意：
    本題沒有提供測試資料組數，
    必須持續讀取輸入直到檔案結束（EOF）。

    實作方式：
    使用 while 迴圈搭配 try-except，
    當 input() 讀不到資料時會觸發 EOFError，進而結束程式。
    """

    try:
        while True:
            # 讀入一行資料，並去除前後空白
            line = input().strip()

            # 若該行為空（例如多餘換行），則跳過
            if not line:
                continue

            # 將該行拆成兩個整數
            first_army, second_army = map(int, line.split())

            # 呼叫函式計算差距
            answer = calculate_difference(first_army, second_army)

            # 輸出結果
            print(answer)

    except EOFError:
        # 當讀取到輸入結束（EOF）時，正常結束程式
        pass


# 程式進入點（確保此檔案被直接執行時才會呼叫 solve）
if __name__ == "__main__":
    solve()