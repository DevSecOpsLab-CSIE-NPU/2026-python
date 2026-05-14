# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter

# 匯入xml.etree.ElementTree模組，用於解析XML資料
import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────
# 定義一個RSS格式的XML字串作為範例資料
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
# 使用ET.fromstring()從字串解析XML，得到根元素
root = ET.fromstring(xml_data)
print("根標籤：", root.tag)           # 輸出根元素的標籤名稱（rss）
print("屬性：",   root.attrib)        # 輸出根元素的屬性字典（{'version': '2.0'}）

# ── find / findall ────────────────────────────────────────
# 使用find()尋找第一個匹配的子元素
channel = root.find("channel")  # 尋找名為"channel"的第一個子元素
print("頻道名稱：", channel.find("title").text)  # 在channel元素下尋找title元素的文字內容

# 使用findall()尋找所有匹配的子元素
# 取得所有item元素
for item in root.findall("channel/item"):  # 尋找所有位於channel下的item元素
    title  = item.find("title").text   # 取得title元素的文字
    author = item.find("author").text  # 取得author元素的文字
    print(f"  [{author}] {title}")     # 格式化輸出

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# 使用iter()方法遍歷整個XML樹中所有指定名稱的元素
print("\n所有 <title>：")
for elem in root.iter("title"):  # 遍歷所有名為"title"的元素（無論在哪個層級）
    print(" ", elem.text)        # 輸出每個title元素的文字內容

# ── 從檔案解析 ───────────────────────────────────────────
# 如果要從檔案解析XML，可以使用ET.parse()方法：
# tree = ET.parse("data.xml")  # 解析XML檔案
# root = tree.getroot()        # 取得根元素

# ── 取得屬性 .get() ───────────────────────────────────────
# 使用.get()方法取得元素的屬性值
version = root.get("version")  # 取得根元素的"version"屬性
print("\nRSS 版本：", version)        # 輸出：2.0
print("不存在的屬性：", root.get("missing", "預設值"))  # 如果屬性不存在，返回預設值
