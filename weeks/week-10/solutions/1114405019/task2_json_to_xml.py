import json
import os
import functools
import time
import xml.etree.ElementTree as ET

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result
    return wrapper

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'output', 'students.json')
XML_PATH = os.path.join(BASE_DIR, 'output', 'students.xml')


@timeit
def read_json(filepath: str) -> dict:
    """讀取 JSON 檔案，回傳 dict"""
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


@timeit
def write_xml(data: dict, filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出"""
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ')
    with open(filepath, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


def build_xml_tree(data: dict) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點"""
    students = data.get('學生清單', [])
    root = ET.Element('students', attrib={
        'source': data.get('來源', ''),
        'total': str(len(students)),
    })
    for s in students:
        ET.SubElement(root, 'student', attrib={
            'id': s.get('學號', ''),
            'dept': s.get('系所名稱', ''),
            'school': s.get('畢業學校', ''),
            'zip': s.get('郵遞區號', ''),
        })
    return root


if __name__ == '__main__':
    data = read_json(JSON_PATH)
    write_xml(data, XML_PATH)
    print(f'已輸出 XML 至 {XML_PATH}')
