import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
import functools
import time
import os

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
    """讀取 JSON 檔案，回傳 dict"""
    with open(filepath, mode='r', encoding='utf-8') as f:
        return json.load(f)

def build_xml_tree(data: dict) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點"""
    root = ET.Element("students")
    root.set("source", data.get("來源", ""))
    root.set("total", str(data.get("總人數", 0)))
    
    for student in data.get("學生清單", []):
        student_el = ET.SubElement(root, "student")
        student_el.set("id", student.get("學號", ""))
        student_el.set("dept", student.get("系所名稱", ""))
        student_el.set("school", student.get("畢業學校", ""))
        student_el.set("zip", student.get("郵遞區號", ""))
        
    return root

@timeit
def write_xml(data: dict, filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出"""
    root = build_xml_tree(data)
    
    # 手動建立帶有無縮進的 XML 以符合簡易輸出或是使用 minidom 來 pretty print
    # 不過為了最原汁原味的形式，可以寫成這樣：
    xml_str = ET.tostring(root, encoding='utf-8')
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ", encoding="utf-8")
    
    # toprettyxml 會加上 XML 宣告 <?xml version="1.0" encoding="utf-8"?>
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='wb') as f:
        f.write(pretty_xml)

def main():
    filepath = "output/students.json"
    if not os.path.exists(filepath):
        print("Error: JSON file not found. Run task1 first.")
        return
        
    data = read_json(filepath)
    write_xml(data, "output/students.xml")

if __name__ == '__main__':
    main()
