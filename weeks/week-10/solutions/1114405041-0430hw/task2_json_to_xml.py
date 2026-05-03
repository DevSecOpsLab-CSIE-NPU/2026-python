from __future__ import annotations

import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


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
def read_json(filepath: str) -> dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def build_xml_tree(data: dict[str, Any]) -> ET.Element:
    source = str(data.get("來源", ""))
    students = data.get("學生清單", [])
    root = ET.Element("students", {"source": source, "total": str(len(students))})

    for item in students:
        ET.SubElement(
            root,
            "student",
            {
                "id": str(item.get("學號", "")),
                "dept": str(item.get("系所名稱", "")),
                "school": str(item.get("畢業學校", "")),
                "zip": str(item.get("郵遞區號", "")),
            },
        )

    return root


@timeit
def write_xml(data: dict[str, Any], filepath: str) -> None:
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    source_json = base_dir / "output" / "students.json"
    output_xml = base_dir / "output" / "students.xml"
    data = read_json(str(source_json))
    write_xml(data, str(output_xml))
    print(f"已輸出 XML：{output_xml}")


if __name__ == "__main__":
    main()
