# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter

import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────
# 【詳解】
# XML 結構為樹狀，用標籤（tag）表達階層關係。
# ElementTree 是 Python 內建的輕量級 XML 解析工具。
# 重型工具如 lxml 功能更強但需另裝。
# 本範例模擬 RSS 訂閱格式（Atom/RSS 常見 XML 結構）。
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
# 【詳解】
# ET.fromstring(str) 將 XML 字串解析成 Element 樹。
# .tag → 標籤名稱（字串）
# .attrib → 標籤屬性（dict，如 {'version': '2.0'}）
# .text → 標籤文字內容（開始標籤到第一個子元素間的文字）
root = ET.fromstring(xml_data)
print("根標籤：", root.tag) # rss
print("屬性：", root.attrib) # {'version': '2.0'}

# ── find / findall ───────────────────────────────────────
# 【詳解】
# find(path) → 第一個符合路徑的子元素（或 None）
# findall(path) → 所有符合路徑的子元素 list（可能為空）
# 路徑語法是 XPath 的子集，如 "channel/title" 表示「channel 底下第一個 title」
channel = root.find("channel")
print("頻道名稱：", channel.find("title").text)

# 取得所有 item
for item in root.findall("channel/item"):
    title = item.find("title").text
    author = item.find("author").text
    print(f" [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# 【詳解】
# iter(tag) → generator，遞迴遍歷整棵樹找所有符合 tag 的元素。
# 與 find/findall 不同，iter 不受路徑限制，能找到各層的同名標籤。
print("\n所有 <title>：")
for elem in root.iter("title"):
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# 【詳解】
# ET.parse(filename) 解析 XML 檔案，回傳 ElementTree 物件。
# tree.getroot() 取得根節點 Element。
# 後續操作與 fromstring() 完全相同。
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 取得屬性 .get() ───────────────────────────────────────
# 【詳解】
# element.get(attrname) → 取得屬性值（str 或 None）
# element.get(attrname, default) → 屬性不存在時回傳 default
version = root.get("version")
print("\nRSS 版本：", version) # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))
