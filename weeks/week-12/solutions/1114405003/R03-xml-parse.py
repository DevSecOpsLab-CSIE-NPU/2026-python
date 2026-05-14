# R03. XML 解析基礎（6.3）
# 主題：使用 xml.etree.ElementTree 進行 XML 解析與基本查詢
# 註解語言：繁體中文（臺灣 zh-TW），並補充每段程式的用途、回傳型別與常見注意事項

import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────
# 這段 XML 文字是教學用資料，不需要另外準備外部檔案。
# XML 的結構是樹狀的：最外層是根節點 `<rss>`，裡面包含 `<channel>`，
# `<channel>` 底下再有 `<title>` 與多個 `<item>`。
# 這種層級結構非常適合用 ElementTree 來做節點查詢。
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
# `ET.fromstring()` 會把 XML 字串直接解析成 Element 物件，也就是整棵樹的根節點。
# 解析成功後，`root` 不是字串，而是可繼續查詢子節點的 XML 節點物件。
root = ET.fromstring(xml_data)

# `root.tag` 代表目前節點名稱；對最外層來說，這裡就是 `rss`。
# `root.attrib` 則是一個 dict，保存該節點的屬性，例如 `version="2.0"`。
print("根標籤：", root.tag)           # rss
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────
# `find()`：尋找第一個符合條件的節點，找不到時會回傳 `None`。
# `findall()`：尋找所有符合條件的節點，回傳一個列表（list-like 結果）。
# 這兩個方法都支援簡單的路徑語法，例如 `channel/item`。
channel = root.find("channel")

# `channel.find("title")` 會找到 `<channel>` 底下的第一個 `<title>`。
# `.text` 代表節點內的文字內容，也就是 `<title>Planet Python</title>` 中的 `Planet Python`。
print("頻道名稱：", channel.find("title").text)

# 取得所有 item
# `root.findall("channel/item")` 會回傳 `<channel>` 底下所有 `<item>` 節點。
# 我們接著逐一取出每個 item 內的標題與作者，示範如何從巢狀 XML 抓資料。
for item in root.findall("channel/item"):
    title  = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# `iter("title")` 會從根節點開始，遞迴遍歷整棵樹中所有名稱為 `title` 的節點。
# 這比手動一層一層找更方便，特別適合「想找所有同名元素」的情境。
print("\n所有 <title>：")
for elem in root.iter("title"):
    # 這裡會依照 XML 中節點出現的順序，逐一印出文字內容。
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# 如果 XML 資料存放在實體檔案中，通常會使用 `ET.parse()`。
# `parse()` 會回傳 `ElementTree` 物件，再透過 `getroot()` 取得根節點。
# 下列程式先註解掉，因為這份教學主要示範字串解析；實務上可改成自己的檔案路徑。
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 取得屬性 `.get()` ───────────────────────────────────────
# `get()` 用來讀取節點屬性，例如 `<rss version="2.0">` 的 `version`。
# 若屬性存在，就回傳對應值；若不存在，可以提供第二個參數作為預設值。
version = root.get("version")
print("\nRSS 版本：", version)        # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))

# ── 常見提醒 ─────────────────────────────────────────────
# - `.text` 取得的是節點文字內容，不是子節點。
# - `find()` 找不到結果時會回傳 `None`，直接接 `.text` 之前要先確認不是 `None`，避免例外。
# - XML 路徑語法與 XPath 類似但不是完整 XPath；此處示範的是 ElementTree 常用的簡化查詢。
# - 若 XML 來自外部來源，需留意編碼、格式錯誤與空節點，實務上通常要加上例外處理。