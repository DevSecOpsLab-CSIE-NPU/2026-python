"""U01 計時裝飾器簡化版。"""

import csv
import functools
import io
import json
import time
import xml.etree.ElementTree as ET


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - start:.6f}s")
        return result

    return wrapper


def build_data(count):
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
    return list(csv.DictReader(io.StringIO(data)))


@timeit
def read_json_data(data):
    return json.loads(data)


@timeit
def read_xml_data(data):
    root = ET.fromstring(data)
    return [row.attrib for row in root.findall("row")]


def main():
    csv_data, json_data, xml_data = build_data(1000)
    read_csv_data(csv_data)
    read_json_data(json_data)
    read_xml_data(xml_data)


if __name__ == "__main__":
    main()
