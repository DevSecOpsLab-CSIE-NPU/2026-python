"""
R01 easy 版：用最短套路記憶 unittest 常見題。
"""


def make_url(host, domain):
    # 組字串後直接印出。
    print(f"https://{host}.{domain}")


def to_int(text):
    # 空字串就丟錯，其餘用 int。
    if text == "":
        raise ValueError("空字串無法轉成整數")
    return int(text)


def get_user(api, user_id):
    # 讓 api 從外面傳進來，測試時可改成 mock。
    return api.get(f"/users/{user_id}")
