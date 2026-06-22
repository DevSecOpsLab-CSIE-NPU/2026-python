import argparse
import sys
import time
import json
import os
from pathlib import Path

# 將父目錄加入模組搜尋路徑，讓 easy 版可在子目錄中直接執行
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from timing import timeit
from search import linear_search
from search import binary_search
from plot import draw_radar

DEFAULT_SUFFIX = 36

def linear_search_counted(data, target):

    comps = 0
    for i, v in enumerate(data):
        comps += 1
        if v == target:
            return i, comps
    return -1, comps

def binary_search_counted(data, target):
    lo = 0
    hi = len(data) - 1
    comps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1
        if data[mid] == target:
            return mid, comps
        elif data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comps

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100000, help='陣列長度')
    parser.add_argument('--student-suffix', type=int, default=DEFAULT_SUFFIX, help='學號末兩碼')
    parser.add_argument('--repeat', type=int, default=3, help='測試重複次數')
    args = parser.parse_args()

    n = args.n
    arr = list(range(n))  
    K = 100 + (args.student_suffix % 100)

    print('產生陣列長度', n)
    print('目標 K=', K)

    def measure(func):
        records = []
        last_idx, last_cmp = None, None
        for _ in range(args.repeat):
            start = time.perf_counter()
            idx, cmp = func(arr, K)
            end = time.perf_counter()
            records.append(end - start)
            last_idx, last_cmp = idx, cmp
        return sum(records) / len(records), last_idx, last_cmp

    lt, li, lc = measure(linear_search_counted)
    bt, bi, bc = measure(binary_search_counted)

    results = {
        'n': n,
        'target': K,
        'linear': {'index': li, 'comparisons': lc, 'time': lt},
        'binary': {'index': bi, 'comparisons': bc, 'time': bt},
        'faster': 'linear' if lt < bt else 'binary'
    }

    os.makedirs('assets', exist_ok=True)
    with open('assets/results_easy.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    metrics = {
        'linear': {'time': results['linear']['time'], 'comparisons': results['linear']['comparisons'], 'n': n},
        'binary': {'time': results['binary']['time'], 'comparisons': results['binary']['comparisons'], 'n': n}
    }
    draw_radar(metrics, 'assets/radar_easy.png')

    print('Linear:', results['linear'])
    print('Binary:', results['binary'])
    print('Faster:', results['faster'])

if __name__ == '__main__':
    main()
