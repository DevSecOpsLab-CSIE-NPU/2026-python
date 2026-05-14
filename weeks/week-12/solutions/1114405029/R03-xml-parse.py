# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter

# 匯入 xml.etree.ElementTree 模組
# ElementTree 是 Python 內建的 XML 處理工具
# 常用來：
# 1. 解析 XML 文件
# 2. 讀取 XML 標籤與屬性
# 3. 建立 XML 資料
# 4. 處理 RSS、設定檔、資料交換格式

# ET 是常見縮寫
# 後面可以用 ET.xxx 呼叫功能
import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────

# xml_data 是一個多行字串
# 內容是一份 XML 文件

# XML 結構類似樹狀：
# rss
# └── channel
#     ├── title
#     ├── item
#     │   ├── title
#     │   ├── link
#     │   └── author
#     └── item
#         ├── title
#         ├── link
#         └── author

# <rss version="2.0">
# 代表 rss 標籤有一個屬性 version

# <title>文字</title>
# title 是標籤
# 中間的文字稱為 text
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

# ET.fromstring()：
# 將 XML 字串解析成 Element 物件

# root 代表 XML 最外層根節點
# 這裡 root 對應的是 <rss>
root = ET.fromstring(xml_data)

# root.tag：
# 取得目前元素的標籤名稱
# 這裡會得到 "rss"
print("根標籤：", root.tag)           # rss

# root.attrib：
# 取得元素所有屬性
# 回傳型態是 dictionary
# {'version': '2.0'}
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────

# root.find("channel")：
# 尋找第一個符合的 channel 標籤

# 如果找到：
# 回傳 Element 物件

# 如果找不到：
# 回傳 None
channel = root.find("channel")

# channel.find("title")：
# 在 channel 裡尋找 title 標籤

# .text：
# 取得標籤中的文字內容

# 所以：
# <title>Planet Python</title>
# 的 text 是 "Planet Python"
print("頻道名稱：", channel.find("title").text)

# 取得所有 item

# root.findall("channel/item")：
# 尋找所有符合路徑的 item 標籤

# findall() 會回傳 list
# 裡面每個元素都是 Element 物件
for item in root.findall("channel/item"):

    # item.find("title").text：
    # 取得 item 底下 title 的文字內容
    title  = item.find("title").text

    # item.find("author").text：
    # 取得作者名稱
    author = item.find("author").text

    # 使用 f-string 格式化輸出
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────

# 印出區塊標題
print("\n所有 <title>：")

# root.iter("title")：
# 遍歷整棵 XML 樹中所有 title 標籤

# 不管 title 在哪一層，都會被找到
for elem in root.iter("title"):

    # elem.text：
    # 取得 title 標籤中的文字
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────

# ET.parse("data.xml")：
# 從 XML 檔案讀取資料

# tree：
# 代表整棵 XML 文件樹

# tree.getroot()：
# 取得 XML 根節點

# 這裡只是示範，因此先註解起來
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 取得屬性 .get() ───────────────────────────────────────

# root.get("version")：
# 取得 rss 標籤中的 version 屬性

# 等同於：
# root.attrib["version"]

# 但 get() 比較安全
# 不存在時不會報錯
version = root.get("version")

# 印出 RSS 版本
print("\nRSS 版本：", version)        # 2.0

# root.get("missing", "預設值")：

# 如果屬性不存在：
# 回傳第二個參數指定的預設值

# 這裡 missing 屬性不存在
# 所以會輸出 "預設值"
print("不存在的屬性：", root.get("missing", "預設值"))