import sys

def digit_to_char(d):
    """將數字 0~35 轉成字元 '0'~'9', 'A'~'Z'"""
    return chr(ord('0') + d) if d < 10 else chr(ord('A') + d - 10)

def cost_in_base(n, base, costs):
    """計算數字 n 在指定進位制下的印刷成本"""
    if n == 0:
        return costs[0]
    total = 0
    while n > 0:
        total += costs[n % base]
        n //= base
    return total

def cheapest_bases(costs, n):
    """回傳印刷數字 n 成本最低的所有進位制（2~36）"""
    min_cost = float('inf')
    result = []
    for b in range(2, 37):
        c = cost_in_base(n, b, costs)
        if c < min_cost:
            min_cost = c
            result = [b]
        elif c == min_cost:
            result.append(b)
    return result

def parse_input(data):
    """解析輸入字串，回傳 [(costs, queries), ...] 列表"""
    lines = data.strip().splitlines()
    t = int(lines[0])
    idx = 1
    cases = []
    for _ in range(t):
        costs = []
        for _ in range(4):
            costs.extend(map(int, lines[idx].split()))
            idx += 1
        q = int(lines[idx])
        idx += 1
        queries = []
        for _ in range(q):
            queries.append(int(lines[idx]))
            idx += 1
        cases.append((costs, queries))
    return cases

def format_output(case_no, results):
    """依照題目格式輸出"""
    out = [f"Case {case_no}:"]
    for num, bases in results:
        out.append(f"Cheapest base(s) for number {num}: " + " ".join(map(str, bases)))
    return "\n".join(out) + "\n"

def solve():
    """主程式：讀入、計算、輸出"""
    data = sys.stdin.read()
    cases = parse_input(data)
    output_parts = []
    for i, (costs, queries) in enumerate(cases, 1):
        results = []
        for q in queries:
            results.append((q, cheapest_bases(costs, q)))
        output_parts.append(format_output(i, results))
    sys.stdout.write("\n".join(output_parts))

if __name__ == "__main__":
    solve()
