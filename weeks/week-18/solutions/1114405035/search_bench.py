import sys
import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def linear_search(data: list, target: int) -> tuple[int, int]:
    cmp = 0
    for idx, val in enumerate(data):
        cmp += 1
        if val == target:
            return idx, cmp
    return -1, cmp

def binary_search(data: list, target: int) -> tuple[int, int]:
    left = 0
    right = len(data) - 1
    cmp = 0
    while left <= right:
        cmp += 1
        mid = (left + right) // 2
        if data[mid] == target:
            return mid, cmp
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, cmp

def generate_radar_chart(metrics: dict, output_path: str) -> None:
    labels = list(metrics.keys())
    num_vars = len(labels)
    
    linear_vals = [metrics[label][0] for label in labels]
    binary_vals = [metrics[label][1] for label in labels]
    
    linear_vals = np.concatenate((linear_vals, [linear_vals[0]]))
    binary_vals = np.concatenate((binary_vals, [binary_vals[0]]))
    
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, linear_vals, color='#FF5733', linewidth=2, label='Linear Search')
    ax.fill(angles, linear_vals, color='#FF5733', alpha=0.25)
    
    ax.plot(angles, binary_vals, color='#33FF57', linewidth=2, label='Binary Search')
    ax.fill(angles, binary_vals, color='#33FF57', alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, 10)
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    data = list(range(100000))
    target = 135
    
    idx, cmp = binary_search(data, target)
    if idx != -1:
        print(f"FOUND {idx} cmp={cmp}")
    else:
        print(f"NOT FOUND cmp={cmp}")
        
    linear_times = []
    for _ in range(1000):
        t0 = time.perf_counter()
        linear_search(data, target)
        t1 = time.perf_counter()
        linear_times.append(t1 - t0)
    linear_min = min(linear_times)
    
    binary_times = []
    for _ in range(1000):
        t0 = time.perf_counter()
        binary_search(data, target)
        t1 = time.perf_counter()
        binary_times.append(t1 - t0)
    binary_min = min(binary_times)
    
    print(f"linear : {linear_min:.6f} s")
    print(f"binary : {binary_min:.6f} s")
    if binary_min < linear_min:
        print("=> binary faster")
    else:
        print("=> linear faster")
        
    metrics = {
        "Speed": [1.0, 10.0],
        "Code Simplicity": [10.0, 4.0],
        "No Sort Req": [10.0, 1.0],
        "Space Efficiency": [10.0, 10.0],
        "Worst Case Cmp": [1.0, 10.0]
    }
    
    output_dir = "assets"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    generate_radar_chart(metrics, os.path.join(output_dir, "radar.png"))

if __name__ == '__main__':
    main()
