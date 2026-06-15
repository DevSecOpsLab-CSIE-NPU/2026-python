import json
import xml.etree.ElementTree as ET
import time
import functools
import os

def timeit(func):
    """計時裝飾器"""
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
    """讀取 JSON 檔案並回傳字典"""
    with open(filepath, mode='r', encoding='utf-8') as f:
        return json.load(f)

def build_xml_tree(data: dict) -> ET.Element:
    """根據資料字典建構 ElementTree"""
    # 建立根節點
    root = ET.Element("students")
    root.set("source", str(data.get("來源", "")))
    root.set("total", str(data.get("總人數", "0")))

    # 建立子節點
    for student in data.get("學生清單", []):
        s_elem = ET.SubElement(root, "student")
        s_elem.set("id", str(student.get("學號", "")))
        s_elem.set("dept", str(student.get("系所名稱", "")))
        s_elem.set("school", str(student.get("畢業學校", "")))
        s_elem.set("zip", str(student.get("郵遞區號", "")))

    return root

@timeit
def write_xml(root: ET.Element, filepath: str) -> None:
    """將 ElementTree 寫入 XML 檔案"""
    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # 建立樹並寫入
    tree = ET.ElementTree(root)
    # 使用 indent 進行美化（Python 3.9+）
    ET.indent(tree, space="  ", level=0)
    tree.write(filepath, encoding="utf-8", xml_declaration=True)

def main():
    # 資料來源與輸出路徑
    json_path = "output/students.json"
    xml_path = "output/students.xml"

    if not os.path.exists(json_path):
        print(f"錯誤: 找不到來源檔案 {json_path}，請先執行 Task 1。")
        return

    # 1. 讀取 JSON
    print(f"正在讀取資料: {json_path}")
    data = read_json(json_path)

    # 2. 建構 XML 樹
    root = build_xml_tree(data)

    # 3. 寫出 XML
    write_xml(root, xml_path)
    print(f"資料已成功寫出至: {xml_path}")

if __name__ == "__main__":
    main()
