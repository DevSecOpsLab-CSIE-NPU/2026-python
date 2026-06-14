import json
import xml.etree.ElementTree as ET
import functools
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "output", "students.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "students.xml")


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
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def build_xml_tree(data: dict) -> ET.Element:
    total = data.get("總人數", 0)
    source = data.get("來源", "")
    root = ET.Element("students", source=source, total=str(total))
    for student in data.get("學生清單", []):
        ET.SubElement(root, "student",
                      id=student.get("學號", ""),
                      dept=student.get("系所名稱", ""),
                      school=student.get("畢業學校", ""),
                      zip=student.get("郵遞區號", ""))
    return root


@timeit
def write_xml(data: dict, filepath: str) -> None:
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding="utf-8", xml_declaration=True)


def main():
    data = read_json(INPUT_PATH)
    write_xml(data, OUTPUT_PATH)
    print(f"完成！XML 已寫入 {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
