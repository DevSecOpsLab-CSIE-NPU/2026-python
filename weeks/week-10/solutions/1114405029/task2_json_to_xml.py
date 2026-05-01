import json
import time
import functools
import xml.etree.ElementTree as ET
from pathlib import Path


def timeit(func):
    """自訂計時裝飾器，用來量測函式執行時間。"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        begin = time.perf_counter()
        value = func(*args, **kwargs)
        cost = time.perf_counter() - begin
        print(f"[timeit] {func.__name__} 耗時 {cost:.6f}s")
        return value
    return inner


@timeit
def read_json(filepath: str) -> dict:
    """讀取 JSON 檔案，回傳 dict。"""
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def build_xml_tree(data: dict) -> ET.Element:
    """將 JSON 資料建立成 XML 根節點。"""
    students = data.get("學生清單", [])

    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(len(students)),
        },
    )

    for student in students:
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
def write_xml(data: dict, filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出。"""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    root = build_xml_tree(data)
    tree = ET.ElementTree(root)

    ET.indent(tree, space="  ", level=0)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    """主程式：讀取 JSON，轉換後輸出 XML。"""
    data = read_json("output/students.json")
    write_xml(data, "output/students.xml")


if __name__ == "__main__":
    main()