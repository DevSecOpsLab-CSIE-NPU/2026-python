# R02-json-basic.py
# 示範 JSON 序列化與反序列化，需處理 Unicode

import json

def json_demo():
    # 原始資料 (包含 Unicode 中文字元)
    data = {
        "title": "Python 練習",
        "author": "林小明",
        "tags": ["編程", "教學", "JSON"],
        "active": True,
        "score": 98.5
    }

    # 序列化: Python dict -> JSON string
    # ensure_ascii=False 才能正確顯示非 ASCII 字元 (如中文)
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    print("--- 序列化結果 ---")
    print(json_str)

    # 反序列化: JSON string -> Python dict
    parsed_data = json.loads(json_str)
    print("\n--- 反序列化後讀取資料 ---")
    print(f"標題: {parsed_data['title']}")
    print(f"作者: {parsed_data['author']}")
    print(f"標籤類型: {type(parsed_data['tags'])}")

if __name__ == "__main__":
    print("=== JSON 與 Unicode 示範 ===")
    json_demo()
