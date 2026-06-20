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

class JSONReadError(Exception):
    pass

@timeit
def read_json(filepath: str) -> dict:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise JSONReadError(f"JSON 格式錯誤: {e}") from e

def build_xml_tree(data: dict) -> ET.Element:
    root = ET.Element("students", source=data.get("來源", ""), total=str(data.get("總人數", 0)))
    for s in data.get("學生清單", []):
        ET.SubElement(root, "student",
                      id=s.get("學號", ""),
                      dept=s.get("系所名稱", ""),
                      school=s.get("畢業學校", ""),
                      zip=s.get("郵遞區號", ""))
    return root

@timeit
def write_xml(data: dict, filepath: str) -> None:
    d = os.path.dirname(filepath)
    if d:
        os.makedirs(d, exist_ok=True)
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    data = read_json("students.json")
    write_xml(data, "students.xml")
