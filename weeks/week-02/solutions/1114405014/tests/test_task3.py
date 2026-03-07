from collections import Counter
print("請輸入紀錄筆數")
n = int(input())
if n >= 0:
    data_list = []
    print("請輸入user、action並以空格分隔")
    for i in range(n):
        name, action = input().split()
        data_list.append((str(name), str(action)))

    counter = Counter(v[0] for v in data_list)
    sorted_data = sorted(counter.items(), key= lambda x: x[1], reverse=True)
    print("統計結果:")
    for key, value in sorted_data:
        print(f"{key}: {value}")

    action_counter = Counter(v[1] for v in data_list)
    top_action = action_counter.most_common(1)
    print(f"Top action: {top_action[0][0]} {top_action[0][1]}")
elif n ==0:
    print("沒有紀錄")
else:
    print("輸入錯誤")

