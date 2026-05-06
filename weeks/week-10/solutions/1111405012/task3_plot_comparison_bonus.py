from pathlib import Path


SOLUTION_DIR = Path(__file__).resolve().parent
BONUS_OUTPUT_PATH = SOLUTION_DIR / "output" / "timing_comparison_bonus.png"
TIMING_SECONDS = {
    "讀取 CSV": 0.002250,
    "寫出 JSON": 0.001564,
    "讀取 JSON": 0.000500,
    "寫出 XML": 0.001542,
}
PROJECTED_TIMING_SECONDS = {
    "讀取 CSV": 0.003150,
    "寫出 JSON": 0.002190,
    "讀取 JSON": 0.000700,
    "寫出 XML": 0.002159,
}
REQUIRED_PACKAGES = "seaborn matplotlib pandas numpy"


def load_plotting_modules():
    try:
        import matplotlib.font_manager as font_manager
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        import seaborn as sns
        from matplotlib import ft2font, patches
    except ModuleNotFoundError as exc:
        missing = exc.name
        raise RuntimeError(
            f"缺少套件：{missing}。請先安裝：python3 -m pip install {REQUIRED_PACKAGES}"
        ) from exc
    return font_manager, plt, np, pd, sns, patches, ft2font


NOTO_CJK_SEARCH_DIRS = [
    "/usr/share/fonts/opentype/noto",
    "/usr/share/fonts/noto-cjk",
    "/usr/share/fonts/truetype/noto",
]
NOTO_CJK_FILENAMES = [
    "NotoSansCJK-Regular.ttc",
    "NotoSerifCJK-Regular.ttc",
    "NotoSansCJK-Bold.ttc",
]


def font_has_chinese_glyph(ft2font, font_path: str) -> bool:
    charmap = ft2font.FT2Font(font_path).get_charmap()
    return ord("測") in charmap and ord("圖") in charmap


def find_noto_cjk_font() -> Path | None:
    for d in NOTO_CJK_SEARCH_DIRS:
        for name in NOTO_CJK_FILENAMES:
            p = Path(d) / name
            if p.exists():
                return p
    return None


def configure_chinese_font(font_manager, plt, ft2font):
    font_path = find_noto_cjk_font()
    if font_path and font_has_chinese_glyph(ft2font, str(font_path)):
        font_manager.fontManager.addfont(str(font_path))
        font_prop = font_manager.FontProperties(fname=str(font_path))
        plt.rcParams["font.family"] = font_prop.get_name()
        plt.rcParams["font.sans-serif"] = [font_prop.get_name()]
        plt.rcParams["axes.unicode_minus"] = False
        return font_prop.get_name(), font_prop
    raise RuntimeError(
        "找不到 fonts-noto-cjk 字型，無法輸出圖表。\n"
        "請先安裝系統套件：sudo apt install fonts-noto-cjk"
    )


def build_dataframe(pd):
    rows = []
    for name, seconds in TIMING_SECONDS.items():
        rows.append({"函式": name, "資料組": "目前實測", "耗時秒數": seconds})
    for name, seconds in PROJECTED_TIMING_SECONDS.items():
        rows.append({"函式": name, "資料組": "放大資料預估", "耗時秒數": seconds})
    return pd.DataFrame(rows)


def apply_gradient_to_bars(ax, np) -> None:
    from matplotlib.patches import Rectangle

    n_steps = 40
    for patch in list(ax.patches):
        w = patch.get_width()
        h = patch.get_height()
        if w <= 0 or h <= 0:
            continue
        x0, y0 = patch.get_x(), patch.get_y()
        rgb = patch.get_facecolor()[:3]
        zorder = patch.get_zorder()
        patch.set_visible(False)
        step_w = w / n_steps
        for i in range(n_steps):
            alpha = 0.30 + 0.70 * (i / (n_steps - 1))
            ax.add_patch(Rectangle(
                (x0 + step_w * i, y0), step_w, h,
                color=rgb, alpha=alpha,
                zorder=zorder, linewidth=0, clip_on=True,
            ))


def draw_smiley(ax, patches) -> None:
    face = patches.Circle(
        (0.07, 0.12),
        0.065,
        transform=ax.transAxes,
        facecolor="#fde68a",
        edgecolor="#92400e",
        linewidth=1.8,
        zorder=5,
    )
    left_eye = patches.Circle((0.045, 0.14), 0.006, transform=ax.transAxes, color="#111827", zorder=6)
    right_eye = patches.Circle((0.095, 0.14), 0.006, transform=ax.transAxes, color="#111827", zorder=6)
    smile = patches.Arc(
        (0.07, 0.115),
        0.065,
        0.04,
        theta1=200,
        theta2=340,
        transform=ax.transAxes,
        color="#111827",
        linewidth=1.6,
        zorder=6,
    )
    ax.add_patch(face)
    ax.add_patch(left_eye)
    ax.add_patch(right_eye)
    ax.add_patch(smile)


def draw_bonus_chart(output_path: str | Path = BONUS_OUTPUT_PATH) -> None:
    font_manager, plt, np, pd, sns, patches, ft2font = load_plotting_modules()
    font_name, font_prop = configure_chinese_font(font_manager, plt, ft2font)
    df = build_dataframe(pd)

    sns.set_theme(style="whitegrid", context="talk")
    fig, ax = plt.subplots(figsize=(12, 9))
    sns.barplot(
        data=df,
        x="函式",
        y="耗時秒數",
        hue="資料組",
        palette=["#2563eb", "#f97316"],
        ax=ax,
    )

    apply_gradient_to_bars(ax, np)
    draw_smiley(ax, patches)

    fastest = df.loc[df["耗時秒數"].idxmin()]
    slowest = df.loc[df["耗時秒數"].idxmax()]
    ax.set_title("Task 1/2 函式耗時比較圖（加分版）", fontsize=19, pad=18, fontproperties=font_prop)
    ax.set_xlabel("函式名稱（右旋轉 90 度）", fontsize=14, fontproperties=font_prop)
    ax.set_ylabel("執行耗時（秒）", fontsize=14, fontproperties=font_prop)
    ax.tick_params(axis="x", rotation=90)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontproperties(font_prop)
    ax.legend(
        title="資料組",
        bbox_to_anchor=(1.01, 1.0),
        loc="upper left",
        prop=font_prop,
        title_fontproperties=font_prop,
    )
    ax.text(
        0.55,
        0.90,
        f"最快：{fastest['函式']} {fastest['耗時秒數']:.6f}s\n"
        f"最慢：{slowest['函式']} {slowest['耗時秒數']:.6f}s\n"
        "結論：優先觀察最慢步驟，再決定是否優化 I/O。",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=12,
        fontproperties=font_prop,
        bbox={"boxstyle": "round,pad=0.45", "facecolor": "#f8fafc", "edgecolor": "#94a3b8"},
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="%.6fs", fontsize=9, padding=3, rotation=90, fontproperties=font_prop)

    fig.text(
        0.99,
        0.02,
        f"中文字型：{font_name}",
        ha="right",
        fontsize=9,
        color="#475569",
        fontproperties=font_prop,
    )
    fig.tight_layout()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"加分圖表已儲存：{output_path.relative_to(SOLUTION_DIR)}")


def main() -> None:
    draw_bonus_chart()


if __name__ == "__main__":
    main()
