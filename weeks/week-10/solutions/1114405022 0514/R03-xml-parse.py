# R03. XML 解析基礎（6.3）
# 本示例展示了使用 xml.etree.ElementTree 解析 XML 的核心方法：
# 1. find()：尋找第一個符合的子元素（路徑為相對路徑）
# 2. findall()：尋找所有符合的元素（支援相對路徑如 "channel/item"）
# 3. iter()：遞迴遍歷所有同名標籤（無論深度，常用於全域搜尋）
# 4. get()：取得元素的屬性值（可設定預設值）
# 5. text：取得元素的文字內容（標籤內的純文字部分）

import xml.etree.ElementTree as ET  # 標準庫：XML 檔案解析

# ── 範例 XML ─────────────────────────────────────────────
# XML (eXtensible Markup Language) 是一種標籤式文字格式，用於結構化資料存儲
# 特點：
#   - 樹狀結構：每個 XML 檔案有唯一的根元素，下有多層子元素
#   - 標籤對稱：開標籤 <tag> 和結束標籤 </tag> 必須配對
#   - 屬性：標籤可附帶屬性，如 <tag attr="value">
#   - 內容：標籤內可包含文字或其他標籤
# 本例為 RSS (Really Simple Syndication) 格式的 XML，用於發佈新聞提要
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
# ET.fromstring() 將 XML 字串解析成元素樹（Element Tree）
# 返回根元素（root element），所有其他元素都是它的後代
root = ET.fromstring(xml_data)
print("根標籤：", root.tag)           # 預期輸出：rss（根元素的標籤名稱）
print("屬性：",   root.attrib)        # 預期輸出：{'version': '2.0'}（元素的所有屬性以 dict 形式）

# ── find / findall ────────────────────────────────────────
# find() 方法：尋找第一個符合條件的子元素（返回 Element 或 None）
# 路徑為相對路徑，如 "channel" 只搜尋直接子元素
channel = root.find("channel")  # 找到第一個 <channel> 元素
print("頻道名稱：", channel.find("title").text)  # 預期：\"Planet Python\"

# findall() 方法：尋找所有符合條件的元素（返回 list）
# 路徑可用 "/" 分隔多層，如 "channel/item" 表示 channel 下的所有 item
# 預期結果：返回 2 個 <item> 元素
for item in root.findall("channel/item"):
    title  = item.find("title").text  # 取得該 item 下的 <title> 文字內容
    author = item.find("author").text  # 取得該 item 下的 <author> 文字內容
    print(f"  [{author}] {title}")  # 預期輸出：[Alice] 討論 Python 型別提示、[Bob] asyncio 最佳實踐

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# iter(tag) 方法：遞迴搜尋整棵樹，找出所有名稱為 tag 的元素
# 與 findall() 不同：iter() 無視路徑限制，無論多深都能找到
# 例如：iter("title") 會找到根元素、channel、和所有 item 下的 <title>
print("\n所有 <title>：")
for elem in root.iter("title"):
    # 預期輸出：3 個 title
    # 1. \"Planet Python\"（在 <channel> 下）
    # 2. \"討論 Python 型別提示\"（第一個 <item> 下）
    # 3. \"asyncio 最佳實踐\"（第二個 <item> 下）
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# 若 XML 來自檔案而非字串，使用 ET.parse(filename) 代替 ET.fromstring()
# ET.parse() 返回 ElementTree 物件，呼叫 .getroot() 取得根元素
# 此方式適合大型 XML 檔案（省記憶體）或直接讀取檔案
# tree = ET.parse("data.xml")  # 從 "data.xml" 檔案解析
# root = tree.getroot()  # 取得根元素

# ── 取得屬性 .get() ───────────────────────────────────────
# .get(attr_name) 方法：取得元素的屬性值（像 dict 的 get）
# 若屬性不存在，預設返回 None（或可設定預設值）
# 例如：<rss version=\"2.0\"> 中，root.get(\"version\") 會返回 \"2.0\"
version = root.get("version")  # 預期：\"2.0\"
print("\nRSS 版本：", version)        # 預期輸出：2.0
print("不存在的屬性：", root.get("missing", "預設值"))  # 預期輸出：預設值（因為 root 沒有 \"missing\" 屬性）
