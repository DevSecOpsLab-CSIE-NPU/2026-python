"""Week 05 in-class: 生成器基礎（好記版）

此版本用較少抽象概念，聚焦在「看得懂、記得住」。
"""


def easy_frange(start, stop, step):
    """用 while 做最直覺的浮點數遞增。"""
    if step <= 0:
        raise ValueError("step 必須大於 0")

    now = start
    while now < stop:
        yield now
        now += step


def easy_countdown(n):
    """簡單倒數生成器。"""
    while n > 0:
        yield n
        n -= 1


def easy_fibonacci(n):
    """回傳前 n 個 Fibonacci 數字（列表版，較容易背）。"""
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def easy_chain(*iterables):
    """把多個列表接在一起。"""
    for it in iterables:
        for item in it:
            yield item


def easy_flatten(items):
    """遞迴攤平巢狀列表。"""
    for x in items:
        if isinstance(x, list):
            yield from easy_flatten(x)
        else:
            yield x


if __name__ == "__main__":
    print("easy_frange:", list(easy_frange(0, 2, 0.5)))
    print("easy_countdown:", list(easy_countdown(3)))
    print("easy_fibonacci:", easy_fibonacci(10))
    print("easy_chain:", list(easy_chain([1, 2], [3, 4], [5, 6])))
    print("easy_flatten:", list(easy_flatten([1, [2, [3, 4]], 5])))
