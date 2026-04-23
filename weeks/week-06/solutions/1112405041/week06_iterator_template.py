# 【August 的惡意：Week 06 隱藏任務】
# 雖無正式題目，但需整理「迭代器應用」模板。
# 實作自定義迭代器與生成器，避免 0py 處刑。

def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
