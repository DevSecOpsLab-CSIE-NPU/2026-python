"""Week 18 Q4: compare linear search and binary search."""

from __future__ import annotations

import math
import sys
import time
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


SEARCH_TARGET = 112
CJK_FONT_FAMILIES = [
    "Heiti TC",
    "Arial Unicode MS",
    "Hiragino Sans",
    "PingFang TC",
    "Noto Sans CJK TC",
    "Microsoft JhengHei",
    "SimHei",
]

plt.rcParams["font.sans-serif"] = CJK_FONT_FAMILIES + plt.rcParams["font.sans-serif"]
plt.rcParams["axes.unicode_minus"] = False


def linear_search(numbers: Sequence[int], target: int) -> Tuple[bool, int, int]:
    """Return found flag, index, and comparison count."""

    comparisons = 0
    for index, value in enumerate(numbers):
        comparisons += 1
        if value == target:
            return True, index, comparisons
    return False, -1, comparisons


def binary_search(numbers: Sequence[int], target: int) -> Tuple[bool, int, int]:
    """Return found flag, index, and comparison count."""

    left = 0
    right = len(numbers) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if numbers[mid] == target:
            return True, mid, comparisons
        comparisons += 1
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, -1, comparisons


def parse_input(tokens: List[str]) -> List[int]:
    if not tokens:
        return list(range(10000))
    m = int(tokens[0])
    numbers = list(map(int, tokens[1 : 1 + m]))
    if len(numbers) < m:
        raise ValueError("not enough input numbers")
    return numbers


def build_radar_scores(linear_time: float, binary_time: float, linear_cmp: int, binary_cmp: int) -> dict:
    def normalize(higher_better: Iterable[float]) -> List[float]:
        values = list(higher_better)
        minimum = min(values)
        maximum = max(values)
        if math.isclose(minimum, maximum):
            return [3.0 for _ in values]
        return [1.0 + 4.0 * (value - minimum) / (maximum - minimum) for value in values]

    speed_scores = normalize([1.0 / linear_time, 1.0 / binary_time])
    comparison_scores = normalize([1.0 / linear_cmp, 1.0 / binary_cmp])

    return {
        "linear": {
            "small_n_speed": 5.0,
            "large_n_speed": 2.0,
            "sorting_required": 5.0,
            "implementation_difficulty": 5.0,
            "worst_case_comparisons": comparison_scores[0],
            "comparisons": comparison_scores[0],
            "space": 5.0,
            "simplicity": 5.0,
            "scalability": 2.0,
        },
        "binary": {
            "small_n_speed": 3.0,
            "large_n_speed": 5.0,
            "sorting_required": 1.0,
            "implementation_difficulty": 3.0,
            "worst_case_comparisons": comparison_scores[1],
            "comparisons": comparison_scores[1],
            "space": 5.0,
            "simplicity": 3.0,
            "scalability": 5.0,
        },
    }


def create_radar_chart(scores: dict, output_path: Path) -> None:
    labels = [
        "small_n_speed",
        "large_n_speed",
        "sorting_required",
        "implementation_difficulty",
        "worst_case_comparisons",
    ]
    linear_values = [scores["linear"][label] for label in labels]
    binary_values = [scores["binary"][label] for label in labels]

    angles = [index / len(labels) * 2 * math.pi for index in range(len(labels))]
    angles.append(angles[0])
    linear_values.append(linear_values[0])
    binary_values.append(binary_values[0])

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True})
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids([angle * 180 / math.pi for angle in angles[:-1]], labels)
    ax.set_ylim(0, 5)
    ax.set_rlabel_position(0)
    ax.plot(angles, linear_values, linewidth=2, label="linear")
    ax.fill(angles, linear_values, alpha=0.15)
    ax.plot(angles, binary_values, linewidth=2, label="binary")
    ax.fill(angles, binary_values, alpha=0.15)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
    fig.suptitle("學號：1114405012", y=0.98)
    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def solve(data: str) -> str:
    tokens = data.split()
    numbers = parse_input(tokens)

    found_linear, idx_linear, cmp_linear = linear_search(numbers, SEARCH_TARGET)
    found_binary, idx_binary, cmp_binary = binary_search(numbers, SEARCH_TARGET)

    assert found_linear == found_binary
    assert idx_linear == idx_binary

    # Measure linear search (100000 runs)
    start = time.perf_counter()
    for _ in range(100000):
        linear_search(numbers, SEARCH_TARGET)
    linear_time = time.perf_counter() - start

    # Measure binary search (100000 runs)
    start = time.perf_counter()
    for _ in range(100000):
        binary_search(numbers, SEARCH_TARGET)
    binary_time = time.perf_counter() - start

    if found_binary:
        first_line = f"FOUND {idx_binary} cmp={cmp_binary}"
    else:
        first_line = f"NOT FOUND cmp={cmp_binary}"

    scores = build_radar_scores(linear_time, binary_time, cmp_linear, cmp_binary)
    create_radar_chart(scores, Path("assets/radar.png"))

    return "\n".join([
        first_line,
        f"linear: {linear_time:.4f} s",
        f"binary: {binary_time:.4f} s",
        f"=> {'binary' if binary_time < linear_time else 'linear'} faster",
    ])


def main() -> None:
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output + "\n")


if __name__ == "__main__":
    main()
