# R03. XML 解析基礎（6.3）
# 本範例示範 xml.etree.ElementTree 的幾個常用功能：
# 1. ET.fromstring：直接從 XML 字串建立樹狀結構
# 2. find / findall：依路徑尋找節點
# 3. iter：遍歷指定標籤的所有節點
# 4. get：讀取元素屬性

import xml.etree.ElementTree as ET

# -----------------------------------------------------------------------------
# 一、範例 XML 資料
# -----------------------------------------------------------------------------
# 這裡用多行字串模擬一份 RSS XML 文件。
# XML 是一種階層式資料格式，常用於設定檔、資料交換、舊式網站摘要等場景。
#
# 這份 XML 的結構大致如下：
# <rss version="2.0">
#   <channel>
#     <title>Planet Python</title>
#     <item>...</item>
#     <item>...</item>
#   </channel>
# </rss>
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

# -----------------------------------------------------------------------------
# 二、從字串解析 XML
# -----------------------------------------------------------------------------
# ET.fromstring() 會把 XML 字串轉成 Element 物件，這個物件就是整棵 XML 樹的根節點。
# 後續所有查找、迭代、取值動作都會從這個 root 開始。
root = ET.fromstring(xml_data)

# root.tag 代表目前節點的標籤名稱。
# root.attrib 代表目前節點的屬性，會以字典形式呈現。
print("根標籤：", root.tag)           # rss
print("屬性：",   root.attrib)        # {'version': '2.0'}

# -----------------------------------------------------------------------------
# 三、find / findall
# -----------------------------------------------------------------------------
# find() 會回傳第一個符合條件的節點。
# 這裡先找到 <channel>，再從 channel 裡找 <title>。
channel = root.find("channel")
print("頻道名稱：", channel.find("title").text)

# findall() 會回傳所有符合條件的節點清單。
# 路徑 "channel/item" 表示：先找 <channel>，再找其底下所有 <item>。
# 每個 item 都是一則新聞或文章條目。
for item in root.findall("channel/item"):
    # item.find("title").text 取得標題文字
    # item.find("author").text 取得作者文字
    title = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# -----------------------------------------------------------------------------
# 四、iter：遍歷所有同名標籤
# -----------------------------------------------------------------------------
# iter("title") 會走訪整棵 XML 樹中所有名為 title 的節點。
# 這比手動一層一層查找更方便，適合想快速收集某種標籤內容的情況。
print("\n所有 <title>：")
for elem in root.iter("title"):
    print(" ", elem.text)

# -----------------------------------------------------------------------------
# 五、從檔案解析 XML
# -----------------------------------------------------------------------------
# 如果 XML 是存在檔案裡，通常會用 ET.parse()。
# parse() 會回傳 ElementTree 物件，再透過 getroot() 取得根節點。
#
# 下面兩行保留作為教學註解，因為本範例使用字串示範，不需要真的讀檔。
# tree = ET.parse("data.xml")
# root = tree.getroot()

# -----------------------------------------------------------------------------
# 六、取得屬性值 get()
# -----------------------------------------------------------------------------
# get() 用來讀取元素屬性。
# 如果屬性不存在，可以提供預設值，避免程式因為拿到 None 而後續出錯。
version = root.get("version")
print("\nRSS 版本：", version)        # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))

# -----------------------------------------------------------------------------
# 補充說明
# -----------------------------------------------------------------------------
# ElementTree 解析 XML 時，常見概念如下：
# - tag：標籤名稱，例如 rss、channel、item、title
# - text：標籤內的文字內容，例如 <title>Planet Python</title>
# - attrib：屬性字典，例如 <rss version="2.0">
#
# 常見使用技巧：
# - find()：找第一個符合的節點
# - findall()：找全部符合的節點
# - iter()：遍歷所有指定標籤
# - get()：讀取屬性值
#
# 當 XML 結構有巢狀層級時，善用路徑字串可以快速定位資料。
