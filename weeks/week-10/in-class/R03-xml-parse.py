# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter
#
# 這個範例示範 Python 內建 xml.etree.ElementTree 的基本讀取方式：
# 1. 從 XML 字串建立樹狀結構。
# 2. 使用 find / findall 找到指定節點。
# 3. 使用 text 讀取標籤內容。
# 4. 使用 iter 走訪所有同名標籤。
# 5. 使用 get 讀取 XML 屬性。

import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────
# 這裡直接用多行字串模擬 XML 文件，方便示範與測試。
# XML 的結構是樹狀的，最外層是 <rss>，底下有 <channel>，再往下是多個 <item>。
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
# fromstring() 會把 XML 字串直接解析成 Element 物件，也就是樹狀結構的根節點。
# 解析後就可以透過 tag、attrib、find、findall 等方法操作內容。
root = ET.fromstring(xml_data)
# root.tag 會回傳根節點標籤名稱，這裡應該是 rss。
print("根標籤：", root.tag)           # rss
# root.attrib 會回傳根節點的屬性字典，這裡可以看到 version="2.0"。
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────
# find() 用來找第一個符合條件的節點。
# 這裡先找到 <channel>，再從 channel 之下找 <title>。
channel = root.find("channel")
# .text 會回傳標籤內的文字內容，也就是 <title>Planet Python</title> 中的 Planet Python。
print("頻道名稱：", channel.find("title").text)

# 取得所有 item
# findall() 會找出所有符合路徑的節點，結果是一個可迭代序列。
# 這裡用 "channel/item" 取得所有新聞項目，逐一讀取標題與作者。
for item in root.findall("channel/item"):
  # item.find("title") 與 item.find("author") 會回傳子節點，接著用 .text 取出內容。
    title  = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────
# iter() 適合在整棵樹中搜尋所有同名標籤，不一定只侷限在某一層。
# 這裡會列出所有 <title>，包含頻道名稱與每篇文章標題。
print("\n所有 <title>：")
for elem in root.iter("title"):
  # elem 代表找到的每一個 title 節點，.text 就是標籤內文。
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# parse() 用來直接從 XML 檔案讀取並建立 ElementTree。
# 如果資料不是字串，而是存放在檔案中，通常會先 parse()，再用 getroot() 取得根節點。
# tree = ET.parse("data.xml")
# root = tree.getroot()

# ── 取得屬性 .get() ───────────────────────────────────────
# get() 用來讀取某個標籤上的屬性值。
# 例如 <rss version="2.0"> 中的 version 屬性，就可以直接用 root.get("version") 取得。
version = root.get("version")
# 如果屬性存在，get() 會回傳實際值；如果不存在，可以提供預設值避免回傳 None。
print("\nRSS 版本：", version)        # 2.0
print("不存在的屬性：", root.get("missing", "預設值"))
