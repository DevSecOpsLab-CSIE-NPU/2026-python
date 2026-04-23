# Easy version - simplified
# Assume single case
N, K = 5, 2
weighings = [
    ([1,2], [3,4], '='),
    ([1,3], [2,5], '<')
]
possible = []
for coin in range(1, N+1):
    for is_light in [True, False]:
        consistent = True
        for left, right, res in weighings:
            if coin in left and coin in right:
                consistent = False
                break
            if coin not in left and coin not in right:
                if res != '=':
                    consistent = False
                    break
            elif coin in left:
                if is_light and res != '<':
                    consistent = False
                    break
                elif not is_light and res != '>':
                    consistent = False
                    break
            elif coin in right:
                if is_light and res != '>':
                    consistent = False
                    break
                elif not is_light and res != '<':
                    consistent = False
                    break
        if consistent:
            possible.append(coin)
print(possible[0] if len(possible) == 1 else 0)