import sys


# 檢查某一枚硬幣在「較重」或「較輕」的假設下，是否能解釋所有秤重結果
def match(coin: int, heavy: bool, weighings: list[tuple[set[int], set[int], str]]) -> bool:
    # 逐筆秤重檢查：如果 coin 是假幣，這筆秤重應該呈現什麼結果？
    for left, right, result in weighings:
        # coin 在左盤：
        # - 如果它是較重假幣，左邊會比較重，所以結果應是 '>'
        # - 如果它是較輕假幣，左邊會比較輕，所以結果應是 '<'
        if coin in left:
            expect = ">" if heavy else "<"
        # coin 在右盤：方向相反
        elif coin in right:
            expect = "<" if heavy else ">"
        # coin 不在這次秤重中，代表這次結果應該保持平衡
        else:
            expect = "="

        # 只要有一筆秤重不符合，就可以直接判定這個假設不成立
        if expect != result:
            return False

    # 所有秤重都符合，代表這個假設可行
    return True


# 直接把輸入切成 token，讓解析更簡單
tokens = iter(sys.stdin.read().split())
# 第一個 token 是測資數量
t = int(next(tokens))
# 收集每一組測資的答案
answers = []

# 逐組處理測資
for _ in range(t):
    # 每組先讀入硬幣數量 N 與秤重次數 K
    n = int(next(tokens))
    k = int(next(tokens))

    # 這一組測資所有的秤重記錄
    weighings = []
    for _ in range(k):
        # 每筆秤重格式：P + 左盤 P 枚 + 右盤 P 枚 + 結果
        p = int(next(tokens))
        # 用 set 儲存左右盤硬幣，方便快速判斷 coin 是否在其中
        left = {int(next(tokens)) for _ in range(p)}
        right = {int(next(tokens)) for _ in range(p)}
        result = next(tokens)
        weighings.append((left, right, result))

    # candidates 存放所有「可能是假幣」的硬幣編號
    candidates = []
    for coin in range(1, n + 1):
        # 逐枚檢查：
        # - 可能是較重假幣
        # - 可能是較輕假幣
        # 只要其中一種情況成立，就先加入候選名單
        if match(coin, True, weighings) or match(coin, False, weighings):
            candidates.append(coin)

    # 若只有唯一一枚硬幣符合條件，就輸出它；否則輸出 0
    answers.append(str(candidates[0]) if len(candidates) == 1 else "0")

# 多組測資之間要用空白行分隔
print("\n\n".join(answers))
