"""雷达图绘制脚本，用于第4题的多维权衡分析

根据存储在 results.json 中的基准测试结果，生成一个雷达图，展示
三种搜索算法（linear_search, binary_search, set_search）的多维权衡。

维度包括：
1. 平均查找时间
2. 内存开销（间接指标）
3. 可扩展性
4. 数据准备成本
5. 实现复杂度

通过对每个算法进行多维度评分，生成可视化的性能比较图。
"""

import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from typing import Dict, List, Tuple
import numpy as np

# 设置中文字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


def normalize_values(values: List[float]) -> List[float]:
    """将值列表归一化到 [0, 1] 范围内"""
    if not values or max(values) == min(values):
        return [0.5] * len(values)
    return [(v - min(values)) / (max(values) - min(values)) for v in values]


def load_results() -> Dict:
    """从 results.json 文件加载基准测试结果"""
    with open("results.json", "r") as f:
        return json.load(f)


def calculate_dimension_scores(results: Dict) -> Tuple[List[str], List[List[float]]]:
    """计算各个算法在各个维度的得分

    返回:
        算法名称列表和维度得分矩阵
    """
    algorithms = ["linear_search", "binary_search", "set_search"]
    dimensions = ["平均查找时间", "内存开销", "可扩展性", "数据准备成本", "实现复杂度"]

    # 初始化得分矩阵
    scores = {algo: [0.0] * len(dimensions) for algo in algorithms}

    # 从基准测试结果中提取数据
    for data_item in results["results"]:
        n = data_item["n"]

        # 根据数据规模计算每个维度
        linear_avg = data_item["linear"]["avg_time"]
        binary_avg = data_item["binary"]["avg_time"]
        set_avg = data_item["set"]["avg_time"]

        # 维度1：平均查找时间（越低越好）
        times = [linear_avg, binary_avg, set_avg]
        norm_times = normalize_values(times)
        for i, algo in enumerate(algorithms):
            scores[algo][0] += norm_times[i] * (1.0 / len(results["results"]))

        # 维度2：内存开销（间接估计）
        # 线性搜索：O(n)空间，复制数据
        # 二分搜索：O(n)空间，需要排序
        # 集合搜索：O(n)空间，创建哈希表
        # 归一化处理
        scores["linear_search"][1] = 0.8  # 需要复制数据，内存开销较大
        scores["binary_search"][1] = 0.7  # 需要排序，内存开销较大
        scores["set_search"][1] = 0.6  # 需要创建哈希表，内存开销适中

        # 维度3：可扩展性（随数据规模增长的表现）
        # 根据n值进行打分
        if n <= 1000:
            scores["linear_search"][2] = 0.7  # 小数据集表现好
            scores["binary_search"][2] = 0.8  # 小数据集表现好
            scores["set_search"][2] = 0.9  # 小数据集表现好
        elif n <= 20000:
            scores["linear_search"][2] = 0.4  # 中等数据集表现差
            scores["binary_search"][2] = 0.8  # 中等数据集表现好
            scores["set_search"][2] = 0.9  # 中等数据集表现好
        else:
            scores["linear_search"][2] = 0.1  # 大数据集表现差
            scores["binary_search"][2] = 0.7  # 大数据集表现一般
            scores["set_search"][2] = 0.8  # 大数据集表现好

        # 维度4：数据准备成本
        # 线性搜索：无需额外准备
        # 二分搜索：需要排序
        # 集合搜索：需要创建哈希表
        scores["linear_search"][3] = 0.9  # 无准备成本
        scores["binary_search"][3] = 0.5  # 需要排序，准备成本适中
        scores["set_search"][3] = 0.7  # 需要创建哈希表，准备成本适中

        # 维度5：实现复杂度
        # 线性搜索：简单易实现
        # 二分搜索：中等复杂度，需要理解二分思想
        # 集合搜索：简单，但需要理解哈希概念
        scores["linear_search"][4] = 0.9  # 最简单实现
        scores["binary_search"][4] = 0.6  # 中等复杂度
        scores["set_search"][4] = 0.7  # 需要理解哈希

    # 对每个算法的每个维度进行平均
    for algo in algorithms:
        for dim_idx in range(len(dimensions)):
            scores[algo][dim_idx] /= len(results["results"])

    return algorithms, list(scores.values())


def plot_radar_chart(algorithms: List[str], scores: List[List[float]]):
    """绘制雷达图"""
    # 维度名称
    categories = ["平均查找时间", "内存开销", "可扩展性", "数据准备成本", "实现复杂度"]

    # 创建更美观的雷达图布局
    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(111, polar=True)

    # 设置雷达图的角度
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # 闭合图形

    # 使用更专业的配色方案
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 经典的matlab配色

    # 绘制每个算法的雷达图
    for i, (algo, algo_scores) in enumerate(zip(algorithms, scores)):
        # 闭合评分
        algo_scores_closed = algo_scores + algo_scores[:1]

        # 绘制线和填充
        ax.plot(angles, algo_scores_closed, 'o-', 
                color=colors[i], linewidth=3, label=algo, 
                markerfacecolor=colors[i], markersize=8)
        ax.fill(angles, algo_scores_closed, color=colors[i], alpha=0.15)

    # 设置雷达图的标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

    # 设置图表标题
    plt.title("搜索算法多维性能雷达图", fontsize=20, fontweight='bold', 
             pad=30, color='#333333')

    # 设置y轴范围和网格
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=10)
    
    # 绘制网格线
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # 绘制同心圆
    ax.spines['polar'].set_color('#cccccc')
    ax.spines['polar'].set_linewidth(1)

    # 设置图例，位置更合理
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.1), 
               frameon=True, fancybox=True, shadow=True,
               fontsize=11, borderpad=1)

    # 在图表中添加一个描述框
    info_text = (
        "算法性能权衡分析:\\n"
        "• 线性搜索：小数据集内存友好，设计简单\\n"
        "• 二分搜索：中等数据集表现优异，需要预处理\\n"
        "• 集合搜索：查找速度快，但内存开销较大"
    )
    
    plt.figtext(0.02, 0.02, info_text, fontsize=10, 
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', 
                          edgecolor='#dddddd', alpha=0.8),
                verticalalignment='bottom')

    # 保存图表，使用更高分辨率
    plt.tight_layout()
    plt.savefig("assets/radar.png", dpi=400, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()


def main():
    """主函数"""
    # 加载结果
    results = load_results()

    # 计算维度得分
    algorithms, scores = calculate_dimension_scores(results)

    # 打印评分结果
    print("各算法维度评分：")
    print("维度:\t", "\t".join([f"{i+1}" for i in range(len(categories))]))
    for algo, algo_scores in zip(algorithms, scores):
        print(f"{algo}:\t", "\t".join([f"{score:.2f}" for score in algo_scores]))

    # 绘制雷达图
    plot_radar_chart(algorithms, scores)

    print("\n雷达图已保存到 assets/radar.png")


if __name__ == "__main__":
    categories = ["平均查找时间", "内存开销", "可扩展性", "数据准备成本", "实现复杂度"]
    main()