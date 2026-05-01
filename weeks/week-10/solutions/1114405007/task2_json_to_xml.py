import json
import os
import functools
import time
import xml.etree.ElementTree as ET

# ── 裝飾器 ────────────────────────────────────────────────────────────────────

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result
    return wrapper

# ── 核心函式 ──────────────────────────────────────────────────────────────────

@timeit
def read_json(filepath: str) -> dict:
    """讀取 JSON 檔案，回傳 dict"""
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def build_xml_tree(data: dict) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點"""
    root = ET.Element(
        "students",
        attrib={
            "source": data.get("來源", ""),
            "total": str(data.get("總人數", 0)),
        },
    )
    for stu in data.get("學生清單", []):
        ET.SubElement(
            root,
            "student",
            attrib={
                "id": str(stu.get("學號", "")),
                "dept": str(stu.get("系所名稱", "")),
                "school": str(stu.get("畢業學校", "")),
                "zip": str(stu.get("郵遞區號", "")),
            },
        )
    return root


@timeit
def write_xml(data: dict, filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出"""
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
        tree.write(f, encoding="utf-8", xml_declaration=False)


# ── 主程式 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "output", "students.json")
    xml_path = os.path.join(base_dir, "output", "students.xml")

    data = read_json(json_path)
    write_xml(data, xml_path)
    print(f"已寫出 {xml_path}，共 {data.get('總人數', 0)} 筆學生資料")
