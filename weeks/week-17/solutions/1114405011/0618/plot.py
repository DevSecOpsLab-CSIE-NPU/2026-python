"""Stage 4 plotting helpers."""

from json import load
from math import pi
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt


AXES = (
    "Query speed",
    "Setup cost",
    "Amortized cost",
)

STRATEGY_FIELDS = {
    "linear": {
        "Query speed": "linear_search_seconds",
        "Setup cost": None,
        "Amortized cost": "linear_search_seconds",
    },
    "binary": {
        "Query speed": "binary_search_seconds",
        "Setup cost": "sort_once_seconds",
        "Amortized cost": "binary_with_sort_seconds",
    },
    "set": {
        "Query speed": "set_search_seconds",
        "Setup cost": "set_build_once_seconds",
        "Amortized cost": "set_with_build_seconds",
    },
}


def load_results(path):
    with Path(path).open("r", encoding="utf-8") as stream:
        return load(stream)


def _latest_row(results):
    rows = results.get("rows", [])
    if not rows:
        raise ValueError("results must include at least one row")
    return rows[-1]


def _normalize_series(row):
    raw_values = {}
    for axis in AXES:
        values = []
        for strategy_fields in STRATEGY_FIELDS.values():
            field_name = strategy_fields[axis]
            value = 0.0 if field_name is None else float(row.get(field_name, 0.0))
            values.append(value)
        max_value = max(values) or 1.0
        raw_values[axis] = [max_value / (value or max_value) for value in values]
    return raw_values


def _build_angles(count):
    angles = [index * 2 * pi / count for index in range(count)]
    return angles + angles[:1]


def plot_results(results, out_path):
    row = _latest_row(results)
    normalized = _normalize_series(row)

    angles = _build_angles(len(AXES))
    figure, axis = plt.subplots(figsize=(7, 7), subplot_kw={"polar": True})

    for strategy_name, strategy_fields in STRATEGY_FIELDS.items():
        series = []
        for axis_name in AXES:
            field_name = strategy_fields[axis_name]
            per_axis_scores = normalized[axis_name]
            strategy_index = list(STRATEGY_FIELDS).index(strategy_name)
            series.append(per_axis_scores[strategy_index])

        series.append(series[0])
        axis.plot(angles, series, linewidth=2, label=strategy_name)
        axis.fill(angles, series, alpha=0.12)

    axis.set_xticks(angles[:-1])
    axis.set_xticklabels(AXES)
    axis.set_ylim(0, 1.05)
    axis.set_title(f"Search trade-offs at n={row['n']}")
    axis.legend(loc="upper right", bbox_to_anchor=(1.28, 1.12))

    output_path = Path(out_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.tight_layout()
    figure.savefig(output_path, dpi=160)
    plt.close(figure)


def main():
    base_path = Path(__file__).resolve().parent
    results_path = base_path / "results.json"
    output_path = base_path / "assets" / "radar.png"
    results = load_results(results_path)
    plot_results(results, output_path)
    print(f"[OK] 雷達圖已成功輸出至 {output_path}")
    return output_path


if __name__ == "__main__":
    main()