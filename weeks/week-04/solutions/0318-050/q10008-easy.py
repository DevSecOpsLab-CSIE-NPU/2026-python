# 檔名: q10008-easy.py
# 這是 UVA 10008 的簡易好記版 (Easy Version)

import sys

# 1. 大絕招：一次把所有測資讀進來，並且全部轉成大寫！
# (因為第一行只會有數字，不會影響我們統計 A-Z 的次數，所以連切分都免了)
text = sys.stdin.read().upper()

results = []

# 2. 直接針對 26 個英文字母進行統計
# 只要記住 chr(65) 是 'A', chr(90) 是 'Z' 即可
for i in range(65, 91):
    char = chr(i)
    count = text.count(char)
    
    if count > 0:
        # 3. 排序小技巧：我們存入 [-次數, 字母] 的組合
        # 加上負號是為了讓 Python 預設的「由小排到大」變成次數的「由大排到小」
        # 當負數次數一樣時，Python 會自動比較第二項 (字母)，剛好就是「字母由小排到大」！
        results.append([-count, char])
        
# 4. 直接呼叫最基礎的 sort()，不用背 lambda 也能完美達成雙重排序！
results.sort()

# 5. 印出結果
for item in results:
    count = -item[0]  # 記得把負號轉回正數
    char = item[1]
    print(f"{char} {count}")