import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "output"
INPUT_JSON = OUTPUT_DIR / "students.json"
OUTPUT_XML = OUTPUT_DIR / "students.xml"


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
    source = str(data.get("來源", ""))
    students = data.get("學生清單", [])

    root = ET.Element(
        "students",
        {
            "source": source,
            "total": str(len(students)),
        },
    )

    for row in students:
        ET.SubElement(
            root,
            "student",
            {
                "id": str(row.get("學號", "")),
                "dept": str(row.get("系所名稱", "")),
                "school": str(row.get("畢業學校", "")),
                "zip": str(row.get("郵遞區號", "")),
            },
        )
    return root


@timeit
def write_xml(data: dict, filepath: str) -> None:
    root = build_xml_tree(data)
    tree = ET.ElementTree(root)
    out_path = Path(filepath)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    data = read_json(str(INPUT_JSON))
    write_xml(data, str(OUTPUT_XML))
    print(f"已輸出：{OUTPUT_XML}")


if __name__ == "__main__":
    main()
