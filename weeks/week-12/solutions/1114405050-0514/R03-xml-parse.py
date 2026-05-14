# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：find / findall / get / text / iter

import xml.etree.ElementTree as ET

# ── 範例 XML ─────────────────────────────────────────────
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
# ET.fromstring() 將 XML 格式的字串解析成 ElementTree 的根節點 (Element 物件)
root = ET.fromstring(xml_data)
# .tag 取得該節點的標籤名稱 (例如此處為 rss)
print("根標籤：", root.tag)           # rss
# .attrib 取得該節點內的所有屬性，並以字典 (dict) 格式回傳 (例如 {'version': '2.0'})
print("屬性：",   root.attrib)        # {'version': '2.0'}

# ── find / findall ────────────────────────────────────────
# .find() 只會找尋並回傳「第一個」符合指定名稱的子節點
channel = root.find("channel")
# .text 屬性可以取得該標籤所包夾的文字內容
print("頻道名稱：", channel.find("title").text)

# 取得所有 item
# .findall() 會回傳所有符合條件的子節點清單，並支援簡單的階層路徑尋找 (如 channel/item)
for item in root.findall("channel/item"):
    title  = item.find("title").text
    author = item.find("author").text
    print(f"  [{author}] {title}")

# ── iter：遍歷所有同名標籤 ───────────────────────────────
print("\n所有 <title>：")
# .iter() 會在整個樹狀結構中（包含所有的子子孫孫節點）尋找所有指定名稱的標籤
for elem in root.iter("title"):
    print(" ", elem.text)

# ── 從檔案解析 ───────────────────────────────────────────
# 若要直接從 XML 檔案讀取，可使用 ET.parse() 取得 tree 物件
# tree = ET.parse("data.xml")
# 再透過 getroot() 方法取得根節點，後續操作就和前面一樣
# root = tree.getroot()

# ── 取得屬性 .get() ───────────────────────────────────────
# .get() 的用法類似字典，專門用來安全地取得標籤上的屬性值
version = root.get("version")
print("\nRSS 版本：", version)        # 2.0
# 如果指定的屬性不存在，可以傳入第二個參數當作預設值，避免程式出錯
print("不存在的屬性：", root.get("missing", "預設值"))
