import sys

# 六元組總和 (a+b+c+d+e=f) - 大一小萌新嘗試版
# 雖然題目編號是 UVA 10071，但教授改了內容！不要寫成位移題！
# 💡 破解思路：直接跑六層迴圈會爆掉，所以我們把 (a+b+c) 先算好存起來。

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    nums = []
    for i in range(1, n + 1):
        nums.append(int(input_data[i]))

    # 第一步：把 a + b + c 的所有組合算出來，並記下次數
    # 這裡我們用字典 (dict) 來存
    abc_dict = {}
    for a in nums:
        for b in nums:
            for c in nums:
                res = a + b + c
                abc_dict[res] = abc_dict.get(res, 0) + 1

    # 第二步：跑 f - d - e，看有沒有在字典裡
    total = 0
    for f in nums:
        for d in nums:
            for e in nums:
                target = f - d - e
                if target in abc_dict:
                    total += abc_dict[target]

    print(total)

if __name__ == "__main__":
    main()
