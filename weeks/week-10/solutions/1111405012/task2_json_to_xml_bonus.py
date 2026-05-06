import xml.etree.ElementTree as ET
from pathlib import Path

from task2_json_to_xml import SOLUTION_DIR, read_json, timeit, write_xml


BONUS_JSON_PATH = SOLUTION_DIR / "output" / "students_bonus.json"
BONUS_XML_PATH = SOLUTION_DIR / "output" / "students_bonus.xml"


def build_bonus_xml_tree(data: dict) -> ET.Element:
    students = data.get("學生清單") or []
    summary = data.get("加分摘要") or {}
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(len(students)),
            "dept_count": str(summary.get("系所數量", 0)),
            "top_dept": str(summary.get("最多學生系所", "")),
        },
    )

    ET.SubElement(
        root,
        "summary",
        {
            "all_rows": str(summary.get("全部資料筆數", 0)),
            "selected_rows": str(summary.get("篩選後筆數", len(students))),
            "selected_ratio": str(summary.get("篩選比例", "0.00%")),
        },
    )

    ranking = ET.SubElement(root, "department_ranking")
    for item in data.get("系所排名", []):
        ET.SubElement(
            ranking,
            "department",
            {
                "rank": str(item.get("名次", "")),
                "name": str(item.get("系所名稱", "")),
                "count": str(item.get("人數", "")),
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
def write_bonus_xml(data: dict, filepath: str | Path = BONUS_XML_PATH) -> None:
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(build_bonus_xml_tree(data))
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    if not BONUS_JSON_PATH.exists():
        raise FileNotFoundError("請先執行 task1_csv_to_json_bonus.py 產生 students_bonus.json")
    data = read_json(BONUS_JSON_PATH)
    write_bonus_xml(data)
    print(f"加分 XML 已儲存：{BONUS_XML_PATH.relative_to(SOLUTION_DIR)}")


if __name__ == "__main__":
    main()
