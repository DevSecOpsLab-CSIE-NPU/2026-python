import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import json


def load_results():
    """從 results.json 文件加載測量結果"""
    try:
        with open("results.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("results.json not found. Please run benchmark.py first.")
        return None


def normalize_values(data, max_values):
    """將值正規化到 0-1 範圍"""
    normalized = {}
    for category in data:
        normalized[category] = data[category] / max_values[category]
    return normalized


def create_radar_chart(results):
    """創建雷達圖可視化"""
    if not results:
        return

    # 選擇一個尺寸進行比較 (使用最大的尺寸)
    size_key = max(results.keys(), key=lambda k: results[k]["data_size"])
    data = results[size_key]

    # 定義雷達圖的維度 (可以自訂)
    categories = [
        "Small_n_Speed",  # 小規模陣列時的速度 (線性更快)
        "Large_n_Speed",  # 大規模陣列時的速度 (二分更快)
        "Setup_Cost",  # 是否需要排序（二分需要）
        "Implementation",  # 實作複雜度 (二分 > 線性)
        "Worst_Case",  # 最壞情況比較次數 (線性 O(n)，二分 O(log n))
    ]

    # 模擬性能數據 (這是示例數據，實際應用中需要從benchmark.py獲取)
    performance_data = {
        "linear": np.array(
            [
                1.0,  # 小規模陣列時的相對速度 (基準值)
                0.3,  # 大規模陣列時的速度
                1.0,  # 實作成本 (需要額外邏輯)
                0.7,  # 複雜度 (線性較簡單)
                1.0,  # 最壞情況 (線性 O(n) > 二分 O(log n))
            ]
        ),
        "binary": np.array(
            [
                0.5,  # 小規模陣列時的速度 (二分較慢)
                1.0,  # 大規模陣列時的速度 (二分較快)
                0.8,  # 實作成本 (二分較複雜)
                1.0,  # 複雜度 (二分較複雜)
                0.3,  # 最壞情況 (二分較好)
            ]
        ),
    }

    # 設置雷達圖
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

    # 雷達圖角度
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()

    # 繪製線性搜尋
    ax.plot(
        angles,
        performance_data["linear"],
        "o-",
        linewidth=2,
        label="Linear Search",
        color="red",
    )
    ax.fill(angles, performance_data["linear"], alpha=0.25, color="red")

    # 繪製二分搜尋
    ax.plot(
        angles,
        performance_data["binary"],
        "s-",
        linewidth=2,
        label="Binary Search",
        color="blue",
    )
    ax.fill(angles, performance_data["binary"], alpha=0.25, color="blue")

    # 設置分類標題
    ax.set_xticks(angles)
    ax.set_xticklabels(categories)

    # 設置極坐標範圍 (0-1)
    ax.set_ylim(0, 1.0)

    # 添加圖例和標題
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    ax.set_title(
        "Search Algorithm Performance Comparison (Radar Chart)", fontsize=14, pad=20
    )

    # 添加網格線
    ax.grid(True)

    # 保存圖片
    plt.savefig("assets/radar.png", dpi=300, bbox_inches="tight")
    plt.close()

    return performance_data, categories


def analyze_results(results):
    """分析並解讀雷達圖的結果"""
    if not results:
        return None

    analysis = []
    size_key = max(results.keys(), key=lambda k: results[k]["data_size"])
    data = results[size_key]

    # 比較速度
    linear_time = data["linear_v2"]
    binary_time = data["binary_v2"]

    if linear_time < binary_time:
        speed_result = "Linear search is faster in this scenario"
    else:
        speed_result = "Binary search is faster in this scenario"

    # 解讀雷達圖
    analysis.append("Radar Chart Analysis:")
    analysis.append(
        "1. Speed Trade-off: Small arrays favor linear search, large arrays favor binary search"
    )
    analysis.append(
        "2. Setup Cost: Binary search requires sorted data, increasing overhead"
    )
    analysis.append(
        "3. Implementation Complexity: Binary search implementation is more complex"
    )
    analysis.append(
        "4. Scalability: Binary search shows better scaling with larger datasets"
    )
    analysis.append(f"5. Performance: {speed_result}")

    return "\n".join(analysis)


def main():
    """主函式"""
    print("Generating radar chart...")

    results = load_results()
    if results:
        performance_data, categories = create_radar_chart(results)
        analysis = analyze_results(results)

        if analysis:
            print("\n" + "=" * 60)
            print("雷達圖分析:")
            print("=" * 60)
            print(analysis)
            print("=" * 60)

        print(f"\nRadar chart saved to assets/radar.png")
    else:
        print("Failed to load results. Please run benchmark.py first.")


if __name__ == "__main__":
    main()
