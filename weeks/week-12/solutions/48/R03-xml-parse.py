# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter

import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────
# 這段 XML 模擬 RSS 資料，方便示範樹狀解析與節點查找。
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

# ── 解析字串 ─────────────────────────────────────────────
# fromstring 會把 XML 字串轉成樹狀結構，root 就是最外層節點。
root = ET.fromstring(xml_data)
print("根標籤：", root.tag)           # rss
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────
channel = root.find("channel")
# find 取得第一個符合的節點，text 則是節點內文字內容。
print("頻道名稱：", channel.find("title").text)

# 取得所有 item
for item in root.findall("channel/item"):
  # find 用來抓子節點，適合逐筆取出欄位。
    title  = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────
print("\n所有 <title>：")
for elem in root.iter("title"):
  # iter 會走訪整棵樹中所有同名標籤。
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 取得屬性 .get() ───────────────────────────────────────
version = root.get("version")
# get 可以直接讀取標籤屬性，第二個參數是找不到時的預設值。
print("\nRSS 版本：", version)        # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))
