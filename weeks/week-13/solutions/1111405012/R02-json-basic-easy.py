"""R02 JSON 基礎讀寫詳細註解版。"""

import json
from pathlib import Path
import tempfile


DATA = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}


def main():
    # dumps = dump string
    # 把 Python 的 dict 轉成 JSON 字串。
    text = json.dumps(DATA, ensure_ascii=False)
    print(text)

    # loads = load string
    # 把 JSON 字串再還原成 Python 物件。
    obj = json.loads(text)
    print(obj["name"], obj["scores"])

    # 如果要處理實際檔案，就用 dump / load。
    # 這裡用 TemporaryDirectory 避免留下額外檔案。
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "data.json"

        # json.dump：把 Python 物件直接寫進檔案。
        with path.open("w", encoding="utf-8") as file:
            json.dump(DATA, file, ensure_ascii=False, indent=2)

        # json.load：把檔案中的 JSON 讀回來。
        with path.open("r", encoding="utf-8") as file:
            loaded = json.load(file)
            print(loaded)


if __name__ == "__main__":
    main()
