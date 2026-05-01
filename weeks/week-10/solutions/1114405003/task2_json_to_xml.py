import json
import os
import xml.etree.ElementTree as ET
import functools
import time


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
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


@timeit
def write_xml(data: dict, filepath: str) -> None:
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    tree.write(filepath, encoding="utf-8", xml_declaration=True)


def build_xml_tree(data: dict) -> ET.Element:
    root = ET.Element("students")
    root.set("source", data.get("來源", ""))
    root.set("total", str(data.get("總人數", 0)))

    for student in data.get("學生清單", []):
        elem = ET.SubElement(root, "student")
        elem.set("id", student.get("學號", ""))
        elem.set("dept", student.get("系所名稱", ""))
        elem.set("school", student.get("畢業學校", ""))
        elem.set("zip", student.get("郵遞區號", ""))

    return root


def main():
    json_path = os.path.join(os.path.dirname(__file__), "output", "students.json")
    xml_path = os.path.join(os.path.dirname(__file__), "output", "students.xml")

    data = read_json(json_path)
    write_xml(data, xml_path)
    print(f"已寫入 XML 至 {xml_path}")


if __name__ == "__main__":
    main()
