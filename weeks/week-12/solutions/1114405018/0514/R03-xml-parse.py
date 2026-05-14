"""R03. XML 解析基礎（6.3）

說明（繁體中文詳細註解）：
- XML 常用於資料交換與設定檔，`xml.etree.ElementTree` 是標準庫提供的輕量解析工具，
  適合簡單 XML 結構的解析與修改。若需處理大量或複雜 XML（命名空間、DTD），
  建議使用更完整的解析器（如 lxml）。

重點函式：
- `ET.fromstring(xml_text)`：從字串建立 Element 樹並回傳根節點（Element）。
- `find()` / `findall()`：查詢子節點；`find` 回傳第一個匹配，`findall` 回傳清單。
- `iter(tag)`：遍歷整個樹所有符合 tag 的元素（遞迴搜尋）。
- `elem.text` / `elem.get('attr')`：存取元素內容與屬性。
"""

import xml.etree.ElementTree as ET


# 範例 XML
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


# 解析字串為 Element（根節點）
root = ET.fromstring(xml_data)
print("根標籤：", root.tag)           # rss
print("屬性：",   root.attrib)        # {'version': '2.0'}


# find / findall：查詢子節點
channel = root.find("channel")
print("頻道名稱：", channel.find("title").text)

# 取得所有 item 節點並讀取內部子標籤（title, author）
for item in root.findall("channel/item"):
    title  = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")


# iter：遍歷整棵樹找到所有 <title> 標籤（包含 channel 的 title 與 item 的 title）
print("\n所有 <title>：")
for elem in root.iter("title"):
    print(" ", elem.text)


# 從檔案解析範例（註解示意）：
# tree = ET.parse("data.xml")
# root = tree.getroot()


# 取得屬性 (.get)：若屬性不存在可回傳預設值
version = root.get("version")
print("\nRSS 版本：", version)        # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))
