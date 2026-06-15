# q_task5_easy.py
# [AI 教學版] 任務五：pickle 序列化快取
# 重點：如何將複雜的 Python 對象存進硬碟並讀取

import pickle
import os

def get_stats(year):
    curr_dir = os.path.dirname(__file__)
    pkl_path = os.path.join(curr_dir, f"output/{year}_stats.pkl")

    if os.path.exists(pkl_path):
        print(f"「從快取載入」：{year}")
        with open(pkl_path, 'rb') as f:
            return pickle.load(f)
    else:
        print(f"「重新計算」：{year}")
        # 模擬計算結果
        data = {'total': 500, 'by_admission': {'甄選': 200}}
        with open(pkl_path, 'wb') as f:
            pickle.dump(data, f)
        return data

if __name__ == "__main__":
    for y in [112, 113, 112]:
        get_stats(y)
