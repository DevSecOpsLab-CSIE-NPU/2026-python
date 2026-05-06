import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path


SOLUTION_DIR = Path(__file__).resolve().parent
DEFAULT_JSON_PATH = SOLUTION_DIR / "output" / "students.json"
DEFAULT_XML_PATH = SOLUTION_DIR / "output" / "students.xml"


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
def read_json(filepath: str | Path) -> dict:
    with open(filepath, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


@timeit
def write_xml(data: dict, filepath: str | Path) -> None:
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def build_xml_tree(data: dict) -> ET.Element:
    students = data.get("學生清單") or []
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


def main() -> None:
    data = read_json(DEFAULT_JSON_PATH)
    write_xml(data, DEFAULT_XML_PATH)
    print(f"XML 已儲存：{DEFAULT_XML_PATH.relative_to(SOLUTION_DIR)}")


if __name__ == "__main__":
    main()
