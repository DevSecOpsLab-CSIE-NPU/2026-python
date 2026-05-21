"""
Task 1: 三年並排長條圖 (112、113、114 學年度各系招生人數)
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib
import numpy as np

# 設定中文字體
matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """
    讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict
    
    Args:
        year: 學年度 (109, 110, 111, 112, 113, 114)
        data_dir: 資料目錄路徑
        
    Returns:
        {系所名稱: 人數} 的字典
    """
    # CSV 檔案名格式
    filename = f"{year}年新生資料庫.csv"
    filepath = data_dir / filename
    
    # 讀取 CSV 檔案，使用 utf-8-sig 編碼處理 BOM
    df = pd.read_csv(filepath, encoding='utf-8-sig')
    
    # 計算每個系所的人數
    dept_counts = df['系所名稱'].value_counts().to_dict()
    
    return dept_counts


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """
    從多年資料中找出任一年曾進前 top_n 的系所清單
    
    Args:
        year_data: {年份: {系所: 人數}} 的嵌套字典
        top_n: 前幾名
        
    Returns:
        符合條件的系所清單
    """
    # 收集所有年份中前 top_n 的系所
    top_depts_set = set()
    
    for year, dept_dict in year_data.items():
        # 按人數排序，取前 top_n
        sorted_depts = sorted(dept_dict.items(), key=lambda x: x[1], reverse=True)
        top_depts = [dept for dept, _ in sorted_depts[:top_n]]
        top_depts_set.update(top_depts)
    
    return sorted(list(top_depts_set))


def plot_grouped_bar_chart(year_data: dict[int, dict], output_path: Path) -> None:
    """
    繪製三年並排長條圖
    
    Args:
        year_data: {年份: {系所: 人數}} 的嵌套字典
        output_path: 輸出圖片路徑
    """
    # 取得 top 8 系所清單
    top_depts = get_top_depts(year_data, top_n=8)
    
    # 準備資料
    years = sorted(year_data.keys())
    dept_year_data = {dept: {year: 0 for year in years} for dept in top_depts}
    
    for year, dept_dict in year_data.items():
        for dept in top_depts:
            dept_year_data[dept][year] = dept_dict.get(dept, 0)
    
    # 建立圖表
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(top_depts))
    width = 0.25  # 三個柱子的寬度
    
    # 繪製三年的柱子
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    year_labels = ['112', '113', '114']
    
    for i, year in enumerate(years):
        values = [dept_year_data[dept][year] for dept in top_depts]
        offset = (i - 1) * width
        ax.bar(x + offset, values, width, label=f'{year}年', color=colors[i])
    
    # 設定軸標籤和標題
    ax.set_xlabel('系所名稱', fontsize=12, fontweight='bold')
    ax.set_ylabel('人數', fontsize=12, fontweight='bold')
    ax.set_title('112-114 學年度各系招生人數比較', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(top_depts, rotation=45, ha='right')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    # 調整布局
    plt.tight_layout()
    
    # 儲存圖表
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"圖表已保存至: {output_path}")
    plt.close()


def main():
    """主程式"""
    # 取得資料路徑 - 從 solution 目錄向上 4 層到 2026-python
    current_file = Path(__file__).resolve()
    # week-13/solutions/1114405017/task1_grouped_bar.py
    # 往上數：task1一層，1114405017兩層，solutions三層，week-13四層，weeks五層，2026-python六層
    data_dir = current_file.parent.parent.parent.parent.parent / "assets" / "stu-data"
    
    # 讀取 112、113、114 年份的資料
    years = [112, 113, 114]
    year_data = {}
    
    for year in years:
        year_data[year] = load_year(year, data_dir)
        print(f"已讀取 {year} 年度資料，共 {len(year_data[year])} 個系所")
    
    # 繪製並保存長條圖
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "task1.png"
    
    plot_grouped_bar_chart(year_data, output_path)
    
    # 打印摘要
    print("\n=== 前八名系所分析 ===")
    top_depts = get_top_depts(year_data, top_n=8)
    for dept in top_depts:
        print(f"{dept}: 112年={year_data[112].get(dept, 0)}, "
              f"113年={year_data[113].get(dept, 0)}, "
              f"114年={year_data[114].get(dept, 0)}")


if __name__ == "__main__":
    main()
