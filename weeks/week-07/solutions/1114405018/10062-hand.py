def solve_count(counts):
    ans = [1]

    for value in range(2, len(counts) + 2):
        c = counts[value - 2]
        insert_index = value - 1 - c
        ans.insert(insert_index, value)

    return ans

def solve_text(text):

    nums = [int(x) for x in text.split()]
    if not nums:
        return ""

    n = nums[0]
    counts = nums[1:1 + (n - 1)]
    result = solve_count(counts)
    return "\n".join(map(str, result))

def main():

    date = sys.stdin.read()
    output = solve_text(date)

    if output:
        sys.stdout.write(output)

if __name__ == "__main__":
    main()
    