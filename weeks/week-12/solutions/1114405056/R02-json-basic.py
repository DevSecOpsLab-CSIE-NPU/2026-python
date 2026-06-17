"""R02: json dumps/loads and dump/load basics."""

import json
from pathlib import Path

data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

s = json.dumps(data)
print(type(s), s)

s_pretty = json.dumps(data, indent=2, sort_keys=True)
print(s_pretty)

obj = json.loads(s)
print(type(obj), obj["name"])

json_path = Path(__file__).with_name("data.json")
with json_path.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with json_path.open("r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

print(json.dumps([1, True, None, "hello"]))
record = {"city": "Penghu", "population": 100000}
print(json.dumps(record, ensure_ascii=False))
print(json.dumps(record, ensure_ascii=True))
