import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6.5))
ax.axis('off')
lines = [
    "PS C:\\Users\\User\\Downloads\\pythonappeal> cd 2026-python/weeks/week-10/solutions/1112405041",
    "",
    "PS ...\\1112405041> python task1_csv_to_json.py",
    "[timeit] read_csv  \u8017\u6642 0.034467s",
    "[timeit] write_json \u8017\u6642 0.001446s",
    "",
    "PS ...\\1112405041> python task2_json_to_xml.py",
    "[timeit] read_json  \u8017\u6642 0.018030s",
    "[timeit] write_xml  \u8017\u6642 0.001274s",
    "",
    "PS ...\\1112405041> python task3_plot_comparison.py",
    "\u5716\u7247\u5df2\u5132\u5b58\uff1atiming_comparison.png",
    "",
    "PS ...\\1112405041> python -m unittest discover -p \"test_*.py\" -v",
    "... (29 tests) ...",
    "Ran 29 tests in 0.187s",
    "OK",
]
text = "\n".join(lines)
ax.text(0.05, 0.95, text, transform=ax.transAxes, fontfamily='Microsoft JhengHei', fontsize=9,
        verticalalignment='top', color='lime')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
plt.tight_layout()
plt.savefig('程式執行.png', dpi=150, bbox_inches='tight', facecolor='black')
print('OK')
