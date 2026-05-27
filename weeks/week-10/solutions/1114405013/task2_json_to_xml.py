from __future__ import annotations
import functools, json, time
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
def read_json(filepath: str | Path) -> dict[str, Any]:
    with Path(filepath).open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("JSON 根資料必須是 dict")
    return data

def build_xml_tree(data: dict[str, Any]) -> ET.Element:
    students = data.get("學生清單", [])
    if not isinstance(students, list):
        raise ValueError("學生清單必須是 list")
    root = ET.Element("students", {"source": str(data.get("來源", "")), "total": str(len(students))})
    for s in students:
        if not isinstance(s, dict):
            raise ValueError("學生資料必須是 dict")
        ET.SubElement(root, "student", {
            "id": str(s.get("學號", "")),
            "dept": str(s.get("系所名稱", "")),
            "school": str(s.get("畢業學校", "")),
            "zip": str(s.get("郵遞區號", "")),
        })
    return root

@timeit
def write_xml(data: dict[str, Any], filepath: str | Path) -> None:
    p = Path(filepath)
    p.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(build_xml_tree(data))
    try:
        ET.indent(tree, space="  ")
    except AttributeError:
        pass
    tree.write(p, encoding="utf-8", xml_declaration=True)

def main() -> None:
    base = Path(__file__).resolve().parent
    data = read_json(base / "output/students.json")
    write_xml(data, base / "output/students.xml")
    print("XML 已儲存：output/students.xml")

if __name__ == "__main__":
    main()
