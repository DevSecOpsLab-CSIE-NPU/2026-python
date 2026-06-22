from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def inverse_score(value: float, best: float, worst: float) -> float:
    """
    Convert a smaller-is-better metric to a 1~5 score.
    """
    if worst == best:
        return 5.0

    normalized = (worst - value) / (worst - best)
    return 1.0 + normalized * 4.0


def make_radar_chart(
    metrics: dict[str, Any],
    output_path: str | Path = "assets/radar.png",
) -> None:
    """
    Create a radar chart comparing linear search and binary search.

    Score rule:
        Higher score is better.
        Time and comparison count use inverse normalization.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    linear_time = float(metrics.get("linear_time", 0.0))
    binary_time = float(metrics.get("binary_time", 0.0))
    linear_cmp = float(metrics.get("linear_cmp", 1.0))
    binary_cmp = float(metrics.get("binary_cmp", 1.0))

    worst_time = max(linear_time, binary_time)
    best_time = min(linear_time, binary_time)

    worst_cmp = max(linear_cmp, binary_cmp)
    best_cmp = min(linear_cmp, binary_cmp)

    labels = [
        "Speed",
        "Comparisons",
        "Simplicity",
        "No Sort Needed",
        "Large Data",
    ]

    linear_scores = [
        inverse_score(linear_time, best_time, worst_time),
        inverse_score(linear_cmp, best_cmp, worst_cmp),
        5.0,
        5.0,
        2.0,
    ]

    binary_scores = [
        inverse_score(binary_time, best_time, worst_time),
        inverse_score(binary_cmp, best_cmp, worst_cmp),
        3.0,
        2.0,
        5.0,
    ]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

    linear_scores += linear_scores[:1]
    binary_scores += binary_scores[:1]
    angles += angles[:1]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, linear_scores, label="Linear Search")
    ax.fill(angles, linear_scores, alpha=0.2)

    ax.plot(angles, binary_scores, label="Binary Search")
    ax.fill(angles, binary_scores, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 5)
    ax.set_title("Search Performance Comparison")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
