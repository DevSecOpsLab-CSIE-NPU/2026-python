import base64
from pathlib import Path

root = Path(__file__).parent
png = root / 'assets' / 'benchmark.png'
out = root / 'assets' / 'benchmark.b64.txt'
data = base64.b64encode(png.read_bytes()).decode('ascii')
out.write_text(data, encoding='utf-8')
print('wrote', out)
