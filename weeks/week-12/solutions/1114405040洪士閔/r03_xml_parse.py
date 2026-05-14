"""R03. XML 解析基礎。

這份版本示範 xml.etree.ElementTree 的常用操作：
find、findall、get、text、iter。
"""

import xml.etree.ElementTree as ET


# 以字串方式準備 XML 內容，方便直接測試解析結果。
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


# fromstring() 直接把 XML 字串轉成樹狀結構。
root = ET.fromstring(xml_data)
print("根標籤：", root.tag)
print("屬性：", root.attrib)


# find() 找第一個符合的子節點。
channel = root.find("channel")
print("頻道名稱：", channel.find("title").text)


# findall() 找出所有符合的節點，適合逐筆處理。
for item in root.findall("channel/item"):
    title = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")


# iter() 會遞迴遍歷所有指定標籤，適合統一抓同名節點。
print("\n所有 <title>：")
for elem in root.iter("title"):
    print(" ", elem.text)


# 若要從檔案解析，可以改用 ET.parse("data.xml")。
# tree = ET.parse("data.xml")
# root = tree.getroot()


# get() 讀取標籤屬性，找不到時可以指定預設值。
version = root.get("version")
print("\nRSS 版本：", version)
print("不存在的屬性：", root.get("missing", "預設值"))
