from collections import Counter

def get_log_data():
    """獲取日誌資料"""
    try:
        n = int(input("請輸入紀錄筆數: "))
        data_list = []
        for i in range(n):
            data = input(f"請輸入第{i+1}筆記錄的user、action（以空格分隔）: ").split()
            if len(data) != 2:
                raise ValueError("輸入格式錯誤，請輸入user action")
            user, action = data
            data_list.append((user, action))
        return data_list
    except ValueError as e:
        print(f"輸入錯誤: {e}")
        return []

def analyze_user_activity(data_list):
    """分析用戶活動統計"""
    user_counter = Counter(user for user, _ in data_list)
    sorted_users = sorted(user_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_users

def analyze_top_action(data_list):
    """分析最常見的動作"""
    action_counter = Counter(action for _, action in data_list)
    if action_counter:
        top_action, count = action_counter.most_common(1)[0]
        return top_action, count
    return None, 0

def display_results(data_list, sorted_users, top_action, top_count):
    if top_action:
        print("\n統計結果（用戶出現次數降序）:")
        for user, count in sorted_users:
            print(f"{user}: {count}")
            print(f"\nTop action: {top_action} {top_count}")
    else:
        print("\n沒有動作記錄")

def main():
    data_list = get_log_data()
    if not data_list:
        return

    sorted_users = analyze_user_activity(data_list)
    top_action, top_count = analyze_top_action(data_list)
    display_results(data_list, sorted_users, top_action, top_count)

if __name__ == "__main__":
    main()
