import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# Timing data recorded from TIMING_REPORT.md
TIMINGS = {
    'read_csv':   0.0,
    'write_json': 0.0,
    'read_json':  0.0,
    'write_xml':  0.0,
}


def plot_comparison(timings: dict, output_path: str) -> None:
    functions = list(timings.keys())
    times = list(timings.values())

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']
    bars = ax.bar(functions, times, color=colors, width=0.5)

    for bar, t in zip(bars, times):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(times) * 0.01,
            f'{t:.5f}s',
            ha='center', va='bottom', fontsize=10,
        )

    ax.set_title('Task 1/2 Function Runtime Comparison', fontsize=13)
    ax.set_xlabel('Function', fontsize=11)
    ax.set_ylabel('Runtime (seconds)', fontsize=11)
    ax.set_ylim(0, max(times) * 1.3 if max(times) > 0 else 0.01)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print('圖表已儲存：output/timing_comparison.png')


if __name__ == '__main__':
    # Import tasks to capture live timings
    import time
    import csv
    import json

    # ── re-run task1 & task2 to collect timings ──────────────
    from task1_csv_to_json import CSV_PATH, JSON_PATH, read_csv, filter_by_admission, count_by_dept, write_json
    from task2_json_to_xml import XML_PATH, read_json, write_xml

    results: dict[str, float] = {}

    def _timed(name, fn, *args, **kwargs):
        start = time.perf_counter()
        out = fn.__wrapped__(*args, **kwargs)   # bypass @timeit's own print
        results[name] = time.perf_counter() - start
        return out

    rows = _timed('read_csv', read_csv, CSV_PATH)
    filtered = filter_by_admission(rows, '聯合登記分發')
    dept_counts = count_by_dept(filtered)
    payload = {
        '來源': '113年新生資料庫',
        '入學方式篩選': '聯合登記分發',
        '總人數': len(filtered),
        '系所統計': dept_counts,
        '學生清單': [
            {'學號': r['學號'], '系所名稱': r['系所名稱'],
             '畢業學校': r['畢業學校'], '郵遞區號': r['郵遞區號']}
            for r in filtered
        ],
    }
    _timed('write_json', write_json, payload, JSON_PATH)

    data = _timed('read_json', read_json, JSON_PATH)
    _timed('write_xml', write_xml, data, XML_PATH)

    for name, t in results.items():
        print(f'[timeit] {name} 耗時 {t:.6f}s')

    plot_comparison(results, os.path.join(OUTPUT_DIR, 'timing_comparison.png'))
