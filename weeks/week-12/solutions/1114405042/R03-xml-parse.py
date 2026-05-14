"""
R03. XML 解析基礎（6.3）

本模組展示 Python 內建 xml.etree.ElementTree 模組的基本 XML 解析用法：
    1. fromstring() - 解析 XML 字串，返回根元素
    2. find() - 查找單個子元素
    3. findall() - 查找所有符合路徑的元素
    4. iter() - 遍歷所有同名的元素
    5. get() - 取得元素的屬性值
    6. text - 取得元素的文字內容

ElementTree 是一種輕量級的 XML 解析方式，適合處理結構化的資料和配置檔案。
相比 DOM 和 SAX，ElementTree 提供了簡潔易用的 API。
"""

import xml.etree.ElementTree as ET  # XML 解析模組，別名為 ET 方便使用

# ── 範例 XML ─────────────────────────────────────────────
# 這是一個模擬的 RSS Feed XML 文檔，包含以下結構：
# - <rss>：根元素，代表整個 RSS Feed，版本為 2.0
# - <channel>：頻道元素，包含頻道的元資訊
# - <title>：標題元素，分別出現在 channel 和 item 中
# - <item>：文章項目元素，每個 item 代表一篇文章
# - <link>：連結元素
# - <author>：作者元素
#
# XML 的層級結構（樹型結構）對應了資料的邏輯關係，
# 解析時需要按照路徑層級進行查找。
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
# ET.fromstring() 將 XML 字串解析為一個 Element 樹結構
# 返回根元素（root element），即 <rss> 標籤
# 返回的 root 物件包含了整個 XML 樹的資訊

root = ET.fromstring(xml_data)  # 解析 XML 字串，取得根元素
print("根標籤：", root.tag)           # 根元素的標籤名稱：rss
print("屬性：",   root.attrib)        # 根元素的屬性字典：{'version': '2.0'}

# ── find / findall ────────────────────────────────────────
# find(path)：查找第一個符合指定路徑的元素，返回 Element 物件或 None
# findall(path)：查找所有符合指定路徑的元素，返回列表
#
# 路徑可以是：
#   - 簡單標籤名："item"（找直接子元素）
#   - 路徑："channel/item"（找 channel 下的 item）
#   - 相對路徑：開頭加 "/"（根目錄）、"./" （當前）或 ".." （父元素）

channel = root.find("channel")  # 找第一個 <channel> 元素
print("頻道名稱：", channel.find("title").text)  # 取得 channel 下的 title 的文字內容

# 取得所有 item
# findall() 返回列表，可以用 for 迴圈遍歷
for item in root.findall("channel/item"):  # 逐一取得每個 <item>
    title  = item.find("title").text  # 取得 <title> 的文字內容
    author = item.find("author").text  # 取得 <author> 的文字內容
    print(f"  [{author}] {title}")  # 格式化輸出

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# iter(tag) 方法會遍歷樹中所有名稱為 tag 的元素（無論層級有多深）
# 這對於需要收集所有同名元素時非常有用
# 不同於 find/findall，iter 不需要指定完整路徑
#
# 在本例中，XML 有多個 <title> 元素：
#   - 1 個在 <channel> 層級
#   - 2 個在 <item> 層級（每個 item 一個）
# iter 會全部找到

print("\n所有 <title>：")
for elem in root.iter("title"):  # 遍歷所有 <title> 元素，無論深度
    print(" ", elem.text)  # 列印每個 title 的文字內容

# ── 從檔案解析 ───────────────────────────────────────────
# 如果 XML 資料在檔案中，可以使用 parse() 方法直接解析檔案
# parse(filename) 返回一個 ElementTree 物件
# 透過 getroot() 方法可以取得根元素
#
# 例如：
# tree = ET.parse("data.xml")  # 解析 XML 檔案
# root = tree.getroot()        # 取得根元素

# ── 取得屬性 .get() ───────────────────────────────────────
# 元素可以有屬性（attributes），儲存在標籤的開始部分
# 例如 <rss version="2.0"> 中，version="2.0" 是屬性
#
# elem.get(key, default=None)：取得指定屬性的值
# 如果屬性不存在，可以提供預設值避免返回 None
#
# 也可以用 elem.attrib 字典來訪問所有屬性

version = root.get("version")  # 取得 <rss> 的 version 屬性值
print("\nRSS 版本：", version)        # 輸出：2.0
print("不存在的屬性：", root.get("missing", "預設值"))  # 屬性不存在則返回預設值
