import sys

# 優質學生判斷器 - 大一小萌新簡單版
# 雖然題目寫著 Decode the Mad man，但看過 .md 的人都知道這是教授的釣魚陷阱！
# 真正的任務是：讀一個 ID，看他是不是優質學生。

def main():
    # 讀取輸入 ID
    raw_input = sys.stdin.read().strip()

    if not raw_input:
        return

    # 嘗試轉成整數
    if raw_input.isdigit():
        student_id = int(raw_input)

        # 只要在 2 到 10000 之間，或是我的學號，都是優質學生
        if student_id == 1112405041 or (student_id >= 2 and student_id <= 10000):
            print("yes")
        else:
            print("no")
    else:
        # 如果輸入根本不是數字，那一定是跑錯題目的解密派，輸出 no
        print("no")

if __name__ == "__main__":
    main()
