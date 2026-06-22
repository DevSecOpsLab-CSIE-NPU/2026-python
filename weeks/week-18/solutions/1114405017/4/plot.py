import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'Noto Sans TC', 'SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

OUTPUT = Path(__file__).resolve().parent / 'radar.png'


def normalize(value: float, max_value: float) -> float:
    """Turn smaller values into larger normalized scores for radar chart comparison."""
    if max_value == 0:
        return 0.0
    return max(0.0, 1.0 - value / max_value)


def create_radar_chart(labels, values_a, values_b, names, output_path: Path) -> None:
    """建立雷達圖，並儲存為 PNG 圖檔。"""
    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_rlabel_position(180 / len(labels))
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['0.25', '0.5', '0.75', '1.0'])
    ax.set_ylim(0, 1.0)

    values_a = values_a + values_a[:1]
    values_b = values_b + values_b[:1]

    ax.plot(angles, values_a, linewidth=2, linestyle='solid', label=names[0])
    ax.fill(angles, values_a, alpha=0.25)
    ax.plot(angles, values_b, linewidth=2, linestyle='dashed', label=names[1])
    ax.fill(angles, values_b, alpha=0.15)

    ax.set_title('線性搜尋 vs 二分搜尋 維度比較', y=1.12)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(output_path), dpi=200, bbox_inches='tight')
    plt.close(fig)


def main() -> None:
    labels = ['比較次數', '執行時間', '複雜度']

    linear_comparisons = 10000
    binary_comparisons = math.log2(10000)
    linear_time = 1.0
    binary_time = 0.05

    max_comparisons = max(linear_comparisons, binary_comparisons)
    max_time = max(linear_time, binary_time)
    max_complexity = max(10000, math.log2(10000))

    linear_scores = [
        normalize(linear_comparisons, max_comparisons),
        normalize(linear_time, max_time),
        normalize(10000, max_complexity),
    ]
    binary_scores = [
        normalize(binary_comparisons, max_comparisons),
        normalize(binary_time, max_time),
        normalize(math.log2(10000), max_complexity),
    ]

    create_radar_chart(labels, linear_scores, binary_scores, ['Linear', 'Binary'], OUTPUT)
    print(f'Radar chart saved to: {OUTPUT}')


if __name__ == '__main__':
    main()
