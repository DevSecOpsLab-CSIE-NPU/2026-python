from sys import stdin


# 先算第 i 位玩家在本輪第一次成功的機率，再除以無限等比級數的總和。
def winning_probability(player_count, success_probability, player_index):
    if success_probability == 0:
        return 0.0

    lose_one_round = (1 - success_probability) ** player_count
    numerator = ((1 - success_probability) ** (player_index - 1)) * success_probability
    denominator = 1 - lose_one_round

    if denominator == 0:
        return 0.0

    return numerator / denominator


# 依序處理所有測資，並格式化為小數點後四位。
def solve(data):
    test_case_count = int(data[0])
    index = 1
    results = []

    for _ in range(test_case_count):
        player_count = int(data[index])
        success_probability = float(data[index + 1])
        player_index = int(data[index + 2])
        index += 3

        probability = winning_probability(player_count, success_probability, player_index)
        results.append(f"{probability:.4f}")

    return "\n".join(results)


def main():
    tokens = stdin.read().split()
    if not tokens:
        return
    print(solve(tokens))


if __name__ == "__main__":
    main()