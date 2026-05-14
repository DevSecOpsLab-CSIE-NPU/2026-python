"""R02. JSON 基礎讀寫（6.2）"""

from __future__ import annotations

import json
from pathlib import Path
import tempfile
from typing import Any


SAMPLE_DATA = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}
CHINESE_RECORD = {"城市": "澎湖", "人口": 100000}


def to_json_text(
    data: Any,
    *,
    ensure_ascii: bool = True,
    indent: int | None = None,
    sort_keys: bool = False,
) -> str:
    """把 Python 物件轉成 JSON 字串。"""
    return json.dumps(data, ensure_ascii=ensure_ascii, indent=indent, sort_keys=sort_keys)


def from_json_text(json_text: str) -> Any:
    """把 JSON 字串還原成 Python 物件。"""
    return json.loads(json_text)


def write_json_file(
    data: Any,
    file_path: str | Path,
    *,
    ensure_ascii: bool = False,
    indent: int = 2,
) -> None:
    """把 JSON 寫入檔案。"""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)


def read_json_file(file_path: str | Path) -> Any:
    """從檔案讀回 JSON。"""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    """印出課堂上示範的 JSON 轉換結果。"""
    json_text = to_json_text(SAMPLE_DATA)
    print(type(json_text), json_text)

    pretty_text = to_json_text(SAMPLE_DATA, indent=4, sort_keys=True)
    print(pretty_text)

    restored = from_json_text(json_text)
    print(type(restored), restored["name"])

    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "data.json"
        write_json_file(SAMPLE_DATA, file_path)
        loaded = read_json_file(file_path)
        print(loaded)

    print(to_json_text([1, True, None, "hello"]))
    print(to_json_text(CHINESE_RECORD, ensure_ascii=False))
    print(to_json_text(CHINESE_RECORD, ensure_ascii=True))


if __name__ == "__main__":
    main()
