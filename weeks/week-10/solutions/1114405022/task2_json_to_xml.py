from __future__ import annotations

import functools
import json
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time

        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_json(filepath: str) -> dict[str, Any]:
    """讀取 JSON 檔案，回傳 dict。"""
    with open(filepath, "r", encoding="utf-8") as file_object:
        return json.load(file_object)


def build_xml_tree(data: dict[str, Any]) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點。"""
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(data.get("總人數", len(data.get("學生清單", [])))),
        },
    )

    for student in data.get("學生清單", []):
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
def write_xml(data: dict[str, Any], filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出。"""
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    if hasattr(ET, "indent"):
        ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def default_input_path() -> Path:
    """回傳 Task 1 輸出的預設 JSON 路徑。"""
    return Path(__file__).resolve().parent / "output" / "students.json"


def default_output_path() -> Path:
    """回傳 Task 2 輸出的預設 XML 路徑。"""
    return Path(__file__).resolve().parent / "output" / "students.xml"


def main() -> None:
    input_path = default_input_path()
    output_path = default_output_path()

    if not input_path.exists():
        raise FileNotFoundError(f"找不到 JSON 檔案：{input_path}")

    data = read_json(str(input_path))
    write_xml(data, str(output_path))
    print(f"已輸出：{output_path}")


if __name__ == "__main__":
    main()