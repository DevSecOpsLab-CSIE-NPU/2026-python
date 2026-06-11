"""UVA 10922 — 2 the 9s 簡單版本"""


def nine_degree_simple(num_str):
    """最簡單的解法"""
    current = num_str
    depth = 0

    while True:
        digit_sum = sum(int(d) for d in current)
        depth += 1
        current = str(digit_sum)

        if len(current) == 1:
            if current == "9":
                return f"{num_str} is a multiple of 9.", depth
            else:
                return f"{num_str} is not a multiple of 9.", 0


if __name__ == "__main__":
    result, depth = nine_degree_simple("9")
    print(f"{result} 深度={depth}")

    result, depth = nine_degree_simple("18")
    print(f"{result} 深度={depth}")

    result, depth = nine_degree_simple("999")
    print(f"{result} 深度={depth}")
