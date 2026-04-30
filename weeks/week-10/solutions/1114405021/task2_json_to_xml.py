import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path


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
    with open(filepath, mode="r", encoding="utf-8") as f:
        return json.load(f)


def build_xml_tree(data: dict) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點"""
    source = str(data.get("來源", ""))
    students = data.get("學生清單", []) or []

    root = ET.Element("students", attrib={"source": source, "total": str(len(students))})

    for student in students:
        ET.SubElement(
            root,
            "student",
            attrib={
                "id": str(student.get("學號", "")),
                "dept": str(student.get("系所名稱", "")),
                "school": str(student.get("畢業學校", "")),
                "zip": str(student.get("郵遞區號", "")),
            },
        )

    return root


@timeit
def write_xml(data: dict, filepath: str) -> None:
    """將 dict 轉換為 XML 並寫出"""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "output" / "students.json"
    output_path = base_dir / "output" / "students.xml"

    data = read_json(str(input_path))
    write_xml(data, str(output_path))
    print(f"XML 已輸出：{output_path.relative_to(base_dir)}")


if __name__ == "__main__":
    main()
