"""U01 計時裝飾器詳細註解版。"""

import csv
import functools
import io
import json
import time
import xml.etree.ElementTree as ET


def timeit(func):
    # 這個裝飾器負責幫任何函式量測執行時間。
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.6f}s")
        return result

    return wrapper


def build_data(count):
    # 建立三種格式但內容相同的資料，方便比較。
    csv_text = "id,name,score\n" + "\n".join(
        f"{i},Student{i:04d},{60 + i % 40}" for i in range(count)
    )
    json_text = json.dumps(
        [{"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40} for i in range(count)]
    )
    xml_text = "<data>" + "".join(
        f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
        for i in range(count)
    ) + "</data>"
    return csv_text, json_text, xml_text


@timeit
def read_csv_data(data):
    # CSV 讀進來後，每列會變成 dict。
    return list(csv.DictReader(io.StringIO(data)))


@timeit
def read_json_data(data):
    # JSON 最直接，loads 一次就能變回 Python 物件。
    return json.loads(data)


@timeit
def read_xml_data(data):
    # XML 先解析成樹，再把每個 row 的屬性抓出來。
    root = ET.fromstring(data)
    return [row.attrib for row in root.findall("row")]


def main():
    csv_data, json_data, xml_data = build_data(1000)
    read_csv_data(csv_data)
    read_json_data(json_data)
    read_xml_data(xml_data)


if __name__ == "__main__":
    main()
