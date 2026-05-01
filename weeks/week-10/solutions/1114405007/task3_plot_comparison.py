import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import pandas as pd

# ── 中文字型設定 ──────────────────────────────────────────────────────────────

def _setup_chinese_font() -> str:
    """找到第一個可用的中文字型並套用，回傳字型名稱。"""
    candidates = [
        "Microsoft JhengHei",   # 微軟正黑體（繁體 Windows）
        "Microsoft YaHei",      # 微軟雅黑（簡體 Windows）
        "Noto Sans TC",         # Noto 繁體
        "DFKai-SB",             # 標楷體
        "SimHei",               # 黑體
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for font in candidates:
        if font in available:
            plt.rcParams["font.family"] = font
            plt.rcParams["axes.unicode_minus"] = False
            return font
    return ""

# ── 耗時資料（Task 1 / Task 2 各自的實測值）──────────────────────────────────

TASK1_TIMING: dict[str, float] = {
    "read_csv":   0.001843,
    "write_json": 0.001376,
}

TASK2_TIMING: dict[str, float] = {
    "read_json": 0.012423,
    "write_xml": 0.001967,
}

# ── 繪圖函式 ──────────────────────────────────────────────────────────────────

def plot_comparison(
    task1: dict[str, float],
    task2: dict[str, float],
    output_path: str,
) -> None:
    font_name = _setup_chinese_font()

    # seaborn 主題
    sns.set_theme(style="whitegrid", palette="muted", font=font_name or "sans-serif")

    all_timing = {**task1, **task2}

    # ── 左圖：Task 1 vs Task 2 分組長條圖 ────────────────────────────────────
    df_group = pd.DataFrame([
        {"函式": k, "耗時 (秒)": v, "Task": "Task 1"}
        for k, v in task1.items()
    ] + [
        {"函式": k, "耗時 (秒)": v, "Task": "Task 2"}
        for k, v in task2.items()
    ])

    # ── 右圖：全部函式耗時排名（橫向 bar）────────────────────────────────────
    df_rank = pd.DataFrame(
        sorted(all_timing.items(), key=lambda x: x[1], reverse=True),
        columns=["函式", "耗時 (秒)"],
    )

    fig, (ax1, ax2) = plt.subplots(
        1, 2,
        figsize=(13, 6),
        gridspec_kw={"width_ratios": [1.4, 1]},
    )
    fig.suptitle(
        "Task 1/2 函式耗時比較",
        fontsize=17, fontweight="bold", y=1.03,
    )

    # ── 左圖繪製 ─────────────────────────────────────────────────────────────
    palette = {"Task 1": "#4C72B0", "Task 2": "#DD8452"}
    sns.barplot(
        data=df_group, x="函式", y="耗時 (秒)", hue="Task",
        palette=palette, ax=ax1, width=0.55,
    )
    ax1.set_title("Task 1 vs Task 2 各函式耗時", fontsize=13, pad=10)
    ax1.set_xlabel("函式名稱", fontsize=11)
    ax1.set_ylabel("耗時（秒）", fontsize=11)
    ax1.legend(title="Task", fontsize=10, title_fontsize=10)

    # 標註數值
    for patch in ax1.patches:
        h = patch.get_height()
        if h > 0:
            ax1.text(
                patch.get_x() + patch.get_width() / 2,
                h + max(all_timing.values()) * 0.015,
                f"{h:.5f}s",
                ha="center", va="bottom", fontsize=9, color="#222222",
            )
    ax1.set_ylim(0, max(all_timing.values()) * 1.3)

    # ── 右圖繪製（耗時排名 / 橫向）────────────────────────────────────────────
    bar_colors = [
        "#C44E52" if v == max(all_timing.values()) else "#5E9E6E"
        for v in df_rank["耗時 (秒)"]
    ]
    bars = ax2.barh(
        df_rank["函式"], df_rank["耗時 (秒)"],
        color=bar_colors, height=0.45,
    )
    ax2.set_title("耗時排名（由高到低）", fontsize=13, pad=10)
    ax2.set_xlabel("耗時（秒）", fontsize=11)
    ax2.set_ylabel("")
    ax2.invert_yaxis()

    for bar, val in zip(bars, df_rank["耗時 (秒)"]):
        ax2.text(
            bar.get_width() + max(all_timing.values()) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.5f}s",
            va="center", fontsize=10, fontweight="bold",
            color="#C44E52" if val == max(all_timing.values()) else "#333333",
        )
    ax2.set_xlim(0, max(all_timing.values()) * 1.35)

    # ── 摘要結論文字框 ────────────────────────────────────────────────────────
    slowest_key = max(all_timing, key=lambda k: all_timing[k])
    summary = (
        f"【結論摘要】\n"
        f"最耗時：{slowest_key}（{all_timing[slowest_key]:.5f}s）\n"
        f"Task 1 合計：{sum(task1.values()):.5f}s　"
        f"Task 2 合計：{sum(task2.values()):.5f}s\n"
        f"read_json 耗時明顯高於其他操作，推測因 JSON 解析需額外記憶體分配。"
    )
    fig.text(
        0.5, -0.03, summary,
        ha="center", va="top", fontsize=10,
        bbox=dict(
            boxstyle="round,pad=0.6",
            facecolor="#f0f4ff",
            edgecolor="#9999cc",
            alpha=0.92,
        ),
    )

    sns.despine(fig=fig)
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"圖表已儲存：{output_path}")
    if font_name:
        print(f"使用中文字型：{font_name}")


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    output_path = os.path.join(base_dir, "output", "timing_comparison.png")
    plot_comparison(TASK1_TIMING, TASK2_TIMING, output_path)
