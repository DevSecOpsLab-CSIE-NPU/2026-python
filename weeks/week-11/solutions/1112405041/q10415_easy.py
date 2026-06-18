# AI Easy 版: 10415 Eb Alto Saxophone Player
import sys

# 每個音符對應的手指按鍵 (1-10)
# '1' 表示按下，'0' 表示放開
FINGERS = {
    'c': '0111001111', 'd': '0111001110', 'e': '0111001100', 'f': '0111001000',
    'g': '0111000000', 'a': '0110000000', 'b': '0100000000', 'C': '0010000000',
    'D': '1111001110', 'E': '1111001100', 'F': '1111001000', 'G': '1111000000',
    'A': '1110000000', 'B': '1100000000'
}

def solve():
    """
    計算每根手指按下的次數。
    規則：只有從 0 變 1 時才計算一次。
    """
    lines = sys.stdin.read().splitlines()
    if not lines: return

    try:
        t_cases = int(lines[0])
    except ValueError: return

    for i in range(1, t_cases + 1):
        if i >= len(lines): melody = ""
        else: melody = lines[i]

        counts = [0] * 10
        prev_state = "0000000000"

        for note in melody:
            curr_state = FINGERS[note]
            for j in range(10):
                # 只有當前為 1 且前一個為 0 時，才算按壓一次
                if curr_state[j] == '1' and prev_state[j] == '0':
                    counts[j] += 1
            prev_state = curr_state

        print(*(counts))

if __name__ == "__main__":
    solve()
