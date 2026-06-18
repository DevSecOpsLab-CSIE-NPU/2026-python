# -*- coding: utf-8 -*-
import os
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # 設為無 GUI 模式以防 headless 環境崩潰
import matplotlib.pyplot as plt
import numpy as np

def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """
    讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict。
    讀檔時請使用 encoding='utf-8-sig'（CSV 有 BOM）。
    每個 row 代表一名學生，因此我們統計各系所出現的次數。
    """
    file_path = data_dir / f"{year}年新生資料庫.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"找不到檔案: {file_path}")
        
    counts = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row.get("系所名稱", "").strip()
            if dept:
                counts[dept] = counts.get(dept, 0) + 1
    return counts

def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """
    從多年資料中找出任一年曾進前 top_n 的系所清單。
    """
    top_depts = set()
    for year, counts in year_data.items():
        # 依人數降序排序，人數相同時依系所名稱升序排序
        sorted_depts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        # 取得前 top_n 名
        for dept, _ in sorted_depts[:top_n]:
            top_depts.add(dept)
    # 回傳排序後的系所清單（字母/筆畫順序），以維持穩定性
    return sorted(list(top_depts))

def main():
    # 尋找資料目錄
    curr = Path(__file__).resolve()
    data_dir = None
    while curr.parent != curr:
        temp_dir = curr / "assets" / "stu-data"
        if temp_dir.exists():
            data_dir = temp_dir
            break
        curr = curr.parent

    if data_dir is None:
        data_dir = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"
        
    # 讀取 112, 113, 114 三年的資料
    years = [112, 113, 114]
    year_data = {}
    for y in years:
        year_data[y] = load_year(y, data_dir)
        
    # 取得任一年曾進前 8 名的系所清單
    target_depts = get_top_depts(year_data, top_n=8)
    
    # 為了讓圖表呈現美觀，我們將這些系所按照三年總人數從大到小排序
    def get_total_count(dept):
        return sum(year_data[y].get(dept, 0) for y in years)
    
    target_depts.sort(key=get_total_count, reverse=True)
    
    # 設定字型以支援中文顯示
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'DFKai-SB', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 圖表尺寸與版面設定
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    
    num_depts = len(target_depts)
    y_indices = np.arange(num_depts)
    bar_height = 0.25
    
    # 準備繪圖數據
    counts_112 = [year_data[112].get(dept, 0) for dept in target_depts]
    counts_113 = [year_data[113].get(dept, 0) for dept in target_depts]
    counts_114 = [year_data[114].get(dept, 0) for dept in target_depts]
    
    # 使用高級和諧的莫蘭迪色系/深海色系
    # 112: 深藍, 113: 中藍, 114: 翠綠/深青
    color_112 = '#1A365D'
    color_113 = '#2B6CB0'
    color_114 = '#319795'
    
    # 繪製橫向長條圖
    rects_112 = ax.barh(y_indices - bar_height, counts_112, bar_height, label='112 學年度', color=color_112, edgecolor='none')
    rects_113 = ax.barh(y_indices, counts_113, bar_height, label='113 學年度', color=color_113, edgecolor='none')
    rects_114 = ax.barh(y_indices + bar_height, counts_114, bar_height, label='114 學年度', color=color_114, edgecolor='none')
    
    # 設定 y 軸刻度與標籤
    ax.set_yticks(y_indices)
    ax.set_yticklabels(target_depts, fontsize=10, fontweight='bold')
    ax.invert_yaxis()  # 反轉 y 軸，使人數最多的系所排在最上方
    
    # 設定 X 軸範圍與網格線
    ax.set_xlabel('招生人數 (人)', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_title('112-114 學年度新生入學招生人數比較\n(僅顯示任一年度曾進前 8 名之系所)', fontsize=14, fontweight='bold', pad=15)
    
    # 加上數值標籤
    ax.bar_label(rects_112, padding=3, fontsize=8, color='#4A5568')
    ax.bar_label(rects_113, padding=3, fontsize=8, color='#4A5568')
    ax.bar_label(rects_114, padding=3, fontsize=8, color='#4A5568')
    
    # 美化邊框與網格
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CBD5E0')
    ax.spines['bottom'].set_color('#CBD5E0')
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color='#E2E8F0')
    ax.set_axisbelow(True)
    
    # 設定圖例
    ax.legend(loc='lower right', frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=10)
    
    plt.tight_layout()
    
    # 建立輸出目錄並儲存
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "task1.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"成功產生圖表並儲存至: {output_path}")

if __name__ == "__main__":
    main()
