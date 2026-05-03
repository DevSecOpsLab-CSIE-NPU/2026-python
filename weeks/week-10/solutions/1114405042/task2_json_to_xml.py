"""Task 2：JSON 轉 XML。"""

from __future__ import annotations

import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_JSON = SCRIPT_DIR / "output/students.json"
OUTPUT_XML = SCRIPT_DIR / "output/students.xml"


def timeit(func):
    """計算函式執行時間並印出結果。"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_json(filepath: str) -> dict:
    """讀取 JSON 檔案，回傳 dict。"""

    with open(filepath, encoding="utf-8") as file_handle:
        return json.load(file_handle)


def build_xml_tree(data: dict) -> ET.Element:
    """依照 JSON 資料建構 XML 樹狀結構。"""

    students = data.get("學生清單", [])
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(data.get("總人數", len(students))),
        },
    )
    for student in students:
        ET.SubElement(
            root,
            "student",
            {
                "id": str(student.get("學號", "")),
                "dept": str(student.get("系所名稱", "")),
                "school": str(student.get("畢業學校", "")),
                "zip": str(student.get("郵遞區號", "")),
            },
        )
    return root


@timeit
def write_xml(data: dict, filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出。"""

    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    if hasattr(ET, "indent"):
        ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    """執行 Task 2 的完整轉換流程。"""

    data = read_json(str(INPUT_JSON))
    write_xml(data, str(OUTPUT_XML))
    print(f"XML 已儲存：{OUTPUT_XML.relative_to(SCRIPT_DIR)}")


if __name__ == "__main__":
    main()