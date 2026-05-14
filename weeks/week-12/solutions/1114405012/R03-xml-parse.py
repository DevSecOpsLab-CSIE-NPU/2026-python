# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter

import xml.etree.ElementTree as ET

# 這份示範重點：
# 1) 先把 XML 字串解析成樹狀結構
# 2) 用 find / findall 找節點
# 3) 用 iter 走訪所有同名標籤
# 4) 用 get 讀取屬性（attribute）

# ── 範例 XML ─────────────────────────────────────────────
# 這裡用多行字串直接模擬一份 RSS XML，方便示範解析流程。
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
# fromstring() 會把 XML 文字解析成樹狀結構，回傳根節點。
root = ET.fromstring(xml_data)
# root.tag 代表根節點名稱；root.attrib 代表根節點上的屬性字典。
print("根標籤：", root.tag)           # rss
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────
# find()：找第一個符合條件的節點，找不到會回傳 None。
# 這裡先找到 <channel>，再往下找 <title>。
channel = root.find("channel")
print("頻道名稱：", channel.find("title").text)

# 取得所有 item
# findall()：找出所有符合條件的節點，回傳 list。
# 'channel/item' 是簡單的路徑寫法，表示先進入 channel，再找底下所有 item。
for item in root.findall("channel/item"):
  # .text 會取得標籤內的文字內容。
    title  = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# iter("title") 會走訪整棵樹中所有 <title> 標籤，包含根節點底下各層。
print("\n所有 <title>：")
for elem in root.iter("title"):
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# 如果 XML 來自檔案，可以先 parse 成 tree，再用 getroot() 取得根節點。
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 取得屬性 .get() ───────────────────────────────────────
# get() 用來讀取元素上的屬性值；第二個參數是預設值，
# 當屬性不存在時就回傳預設值，避免出現 None 或額外判斷。
version = root.get("version")
print("\nRSS 版本：", version)        # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))
