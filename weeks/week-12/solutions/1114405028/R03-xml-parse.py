# R03-xml-parse.py
# 完整繁體中文註釋版：示範 xml.etree.ElementTree 解析 XML 的基本用法

import xml.etree.ElementTree as ET

# ── 範例 XML 字串 ─────────────────────────────────────────
xml_data = """
<rss version="2.0">
  <channel>
    <title>Planet Python</title>
    <item>
      <title>討論 Python 型別提示</title>
      <link>https://example.com/1</link>
      <author>Alice</author>
    </item>
    <item>
      <title>asyncio 最佳實踐</title>
      <link>https://example.com/2</link>
      <author>Bob</author>
    </item>
  </channel>
</rss>
"""

# ── 解析 XML 字串成 Element 樹
root = ET.fromstring(xml_data)
print("根標籤：", root.tag)
print("屬性：", root.attrib)

# ── find / findall：取得第一個元素或多個符合元素
channel = root.find("channel")
print("頻道名稱：", channel.find("title").text)

for item in root.findall("channel/item"):
    title = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# ── iter：遍歷整個 XML 樹中所有指定標籤
print("\n所有 <title>：")
for elem in root.iter("title"):
    print(" ", elem.text)

# ── 從檔案解析的範例（註解示範）
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 屬性取得：root.get('version')，若不存在可給預設值
version = root.get("version")
print("\nRSS 版本：", version)
print("不存在的屬性：", root.get("missing", "預設值"))
