"""R01: csv reader/writer and DictReader/DictWriter basics."""

import csv
import io

raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

print("=== csv.reader ===")
f = io.StringIO(raw)
reader = csv.reader(f)
headers = next(reader)
print("headers:", headers)
for row in reader:
    print(row)

print("\n=== csv.DictReader ===")
f = io.StringIO(raw)
for row in csv.DictReader(f):
    print(f"{row['Symbol']:5s} price={row['Price']:>6s} change={row['Change']}")

print("\n=== csv.writer ===")
out = io.StringIO()
writer = csv.writer(out)
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
print(out.getvalue())

print("=== csv.DictWriter ===")
out = io.StringIO()
fields = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(out, fieldnames=fields)
writer.writeheader()
writer.writerow({"Symbol": "AA", "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(out.getvalue())
