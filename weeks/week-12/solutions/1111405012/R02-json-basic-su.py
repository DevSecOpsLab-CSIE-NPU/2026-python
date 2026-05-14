"""R02 JSON 基礎讀寫簡化版。"""

import json
from pathlib import Path
import tempfile


DATA = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}


def main():
    # Python 物件轉 JSON 字串。
    text = json.dumps(DATA, ensure_ascii=False)
    print(text)

    # JSON 字串轉回 Python。
    obj = json.loads(text)
    print(obj["name"], obj["scores"])

    # dump / load 示範檔案讀寫。
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "data.json"
        with path.open("w", encoding="utf-8") as file:
            json.dump(DATA, file, ensure_ascii=False, indent=2)
        with path.open("r", encoding="utf-8") as file:
            print(json.load(file))


if __name__ == "__main__":
    main()
