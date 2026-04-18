import timeit

# ── 字串串接效能比較：+= vs join ─────────────────────────
# 在迴圈內用 += 串接字串，每次都會建立新的 str 物件（O(n²) 複雜度）
# str.join() 先收集所有片段再一次拼合，效率遠優於逐一串接
parts = [f"item{i}" for i in range(1000)]  # 1000 個字串片段


def bad_concat() -> str:
    """逐一 += 串接：慢，因每次迭代都重新分配記憶體。"""
    s = ""
    for p in parts:
        s += p
    return s


def good_join() -> str:
    """join() 一次完成：快，只需一次記憶體分配。"""
    return "".join(parts)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s join: {t2:.3f}s")  # join 通常快數倍


# ── format_map + 缺鍵保護（SafeSub）────────────────────
# format_map 類似 format(**d)，但直接接受 Mapping 物件
# 若模板中有變數名稱在字典中不存在，預設會拋 KeyError
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        """鍵不存在時，保留原始佔位符而非拋例外。"""
        return "{" + key + "}"  # 例：{n} → 仍輸出 {n}


name = "Guido"
s = "{name} has {n} messages."
# vars() 回傳當前局部變數的字典；{n} 不存在 → 保留 {n}
print(s.format_map(SafeSub(vars())))  # Guido has {n} messages.

# ── 再次確認 str 與 bytes 索引差異 ───────────────────────
a = "Hello"   # str
b = b"Hello"  # bytes
print(a[0])   # 'H'（單字元字串）
print(b[0])   # 72（ASCII 整數）

# encode 後的 bytes 仍可使用格式化字串語法（先格式化再編碼）
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))  # b'ACME         100'
