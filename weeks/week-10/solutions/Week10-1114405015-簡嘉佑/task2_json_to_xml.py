from __future__ import annotations

import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"


def timeit(func):
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
    with Path(filepath).open("r", encoding="utf-8") as file:
        return json.load(file)


def build_xml_tree(data: dict) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點。"""
    students = data.get("學生清單", [])
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(len(students)),
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
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    json_path = OUTPUT_DIR / "students.json"
    xml_path = OUTPUT_DIR / "students.xml"
    data = read_json(str(json_path))
    write_xml(data, str(xml_path))
    print(f"已輸出：{xml_path}")


if __name__ == "__main__":
    main()