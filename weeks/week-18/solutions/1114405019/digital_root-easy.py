import sys

BASE = 6  # 學號末兩碼 19，個位 9 查對照表得 base=6


def digital_root_easy(x: int, base: int) -> int:
    """
    數字根的「好記版」寫法：不拆成兩個函式，直接用一個迴圈做到底。

    口訣：只要 x 在 base 進位下還是兩位數以上（也就是 x >= base），
    就把它的每一位數字加起來，變成新的 x，再檢查一次。
    一直重複，直到 x 變成一位數（x < base）為止。

    x=0 的情況：0 < base 一定成立，迴圈完全不會執行，直接回傳 0，
    剛好符合「0 的數字根固定是 0」的規定，不需要額外特例判斷。
    """
    while x >= base:
        # 這裡是「短除法」的概念：每次用 x % base 拿到最右邊一位數字，
        # 再用 x // base 把這一位丟掉，繼續處理剩下的位數，
        # 直到 x 被除到 0，總和就是這一輪所有位數加起來的結果。
        digit_sum = 0
        while x > 0:
            digit_sum += x % base
            x //= base
        x = digit_sum  # 用這一輪算出的總和取代 x，回到外層迴圈再檢查一次
    return x


def main() -> None:
    # 跟手打版一樣讀到 EOF 結束，不是用 0 當終止值
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(digital_root_easy(x, BASE))


if __name__ == "__main__":
    main()
