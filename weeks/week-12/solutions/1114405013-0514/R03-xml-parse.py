# R03. XML 解析基礎（6.3）
# xml.etree.ElementTree：解析 / 搜尋 / 建立 / 寫入
#
# XML（eXtensible Markup Language）是樹狀結構的標記語言。
# Python 內建 xml.etree.ElementTree 可解析、搜尋、建立、寫入 XML。
# 常用操作模式：解析 → 搜尋（find/findall/iter）→ 存取（text/get）

import xml.etree.ElementTree as ET
from typing import Optional, Any


# ════════════════════════════════════════════════════════════
#  準備範例 XML 字串
#  <rss version="2.0">    ← 根元素（含屬性 version）
#    <channel>            ← 子元素
#      <title>...</title> ← 文字內容（text）
#      <item>...</item>   ← 多個相同名稱的子元素
# ════════════════════════════════════════════════════════════

RAW_XML: str = """
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


# ════════════════════════════════════════════════════════════
#  1. 解析字串 / 取得根元素（ET.fromstring）
#  Element 的三個核心屬性：
#    .tag     → 標籤名稱（str）
#    .text    → 標籤內文字（str | None）
#    .attrib  → 屬性字典（dict）
# ════════════════════════════════════════════════════════════

def demo_parse_and_basics(xml: str) -> ET.Element:
    """
    解析 XML 字串，展示 Element 的核心屬性。

    ET.fromstring(xml_str)：
      - 將 XML 字串解析為 ElementTree 的根元素
      - 回傳型別：xml.etree.ElementTree.Element

    Element 的基本屬性：
      elem.tag      → 標籤名稱（如 'rss', 'channel', 'title'）
      elem.text     → 開始與結束標籤間的文字（None 若無文字）
      elem.attrib   → 屬性字典（如 {'version': '2.0'}）
      elem.tail     → 結束標籤後到下一標籤前的文字（較少用）
    """
    print("=== 解析字串（fromstring）與基本屬性 ===")

    root: ET.Element = ET.fromstring(xml)
    print(f"根標籤（tag）：{root.tag}")
    print(f"根屬性（attrib）：{root.attrib}")          # {'version': '2.0'}
    print(f"根文字（text）：{root.text!r}")            # 通常為 None 或空白

    return root


# ════════════════════════════════════════════════════════════
#  2. 搜尋元素：find / findall
#  find(pattern)   → 回傳第一個符合的子元素（Element | None）
#  findall(pattern) → 回傳所有符合的子元素（list[Element]）
#
#  路徑寫法：
#    "tag"           → 直接子元素（只有一層）
#    "channel/title" → 子孫元素（多層路徑，以 / 分隔）
#    "./tag"         → . 代表當前節點（同上效果）
#  find / findall 只搜尋「子孫元素」，不包含當前元素本身。
# ════════════════════════════════════════════════════════════

def demo_find_findall(root: ET.Element) -> None:
    """
    使用 find / findall 搜尋特定元素。

    find(pattern) 的常見用法：
      - root.find("channel")        → 第一個 <channel> 子元素
      - root.find("channel/title")  → channel 底下的第一個 <title>
      - elem.find("author")         → 第一個 <author> 子元素
      - 若找不到則回傳 None

    findall(pattern) 的常見用法：
      - root.findall("channel/item") → channel 底下所有 <item>
      - 回傳空串列（[]）若無符合元素
    """
    print("\n=== find / findall（搜尋元素）===")

    # find：回傳第一個符合的子元素
    channel: Optional[ET.Element] = root.find("channel")
    if channel is not None:
        # 取得頻道名稱
        title_elem: Optional[ET.Element] = channel.find("title")
        if title_elem is not None:
            print(f"頻道名稱（find channel/title）：{title_elem.text}")

    # findall：回傳所有符合的子元素（list）
    # 路徑寫法 "channel/item" 表示從 root 開始找 channel 下的所有 item
    items: list[ET.Element] = root.findall("channel/item")
    print(f"共有 {len(items)} 篇 item：")

    for i, item in enumerate(items, start=1):
        # 再對每個 item 使用 find 取得子元素
        title:  Optional[ET.Element] = item.find("title")
        author: Optional[ET.Element] = item.find("author")
        link:   Optional[ET.Element] = item.find("link")

        t: str = title.text  if title  is not None else "(無標題)"
        a: str = author.text if author is not None else "(無作者)"
        print(f"  [{i}] {a}：{t}")


# ════════════════════════════════════════════════════════════
#  3. iter：遞迴遍歷所有同名標籤（不分層級）
#  elem.iter("tag") → 生成器，逐一回傳所有 tag 為 "tag" 的子孫元素
#  與 findall 的差別：
#    - findall 需指定路徑，只找特定層級
#    - iter 忽略層級，找出所有同名元素
# ════════════════════════════════════════════════════════════

def demo_iter(root: ET.Element) -> None:
    """
    iter(tag)：遞迴遍歷所有指定名稱的元素。

    iter() 不傳參數 → 遍歷所有子孫元素
    iter("tag")     → 只遍歷指定 tag 的元素

    適用場景：當文件結構不固定，或想忽略層級一次取出所有同類元素。
    """
    print("\n=== iter（遞迴遍歷所有 <title>）===")

    # iter("title") 會找出文件中所有名稱為 <title> 的元素
    # 無論它們在哪一層（<channel/title>、<item/title> 等）
    for elem in root.iter("title"):
        print(f"  <{elem.tag}>：{elem.text}")

    # iter() 無參數：遍歷所有元素，展示樹狀結構
    print("\n所有元素列表（iter 無參數）：")
    for elem in root.iter():
        # 根據層級縮排顯示（2 空格 × 層級深度）
        depth: int = len(list(elem.iter()))  # 此寫法不精準
        print(f"  <{elem.tag}>")


# ════════════════════════════════════════════════════════════
#  4. 取得屬性（elem.get）
#  elem.get("attr", default) → 取得屬性值，不存在時回傳 default
#  elem.attrib["attr"]       → 直接存取字典（不存在會拋 KeyError）
# ════════════════════════════════════════════════════════════

def demo_get_attributes(root: ET.Element) -> None:
    """
    使用 .get() 讀取元素屬性。

    .get() 比 .attrib[] 更安全：
      - 屬性存在 → 回傳屬性值
      - 屬性不存在 → 回傳 None 或指定的預設值（不會拋錯）
    """
    print("\n=== 屬性存取（.get()）===")

    # 取得根元素 <rss> 的 version 屬性
    version: Optional[str] = root.get("version")
    print(f"RSS 版本：{version}")                    # 2.0

    # 不存在的屬性，可提供預設值
    missing: str = root.get("missing", "預設值")
    print(f"不存在的屬性（有預設值）：{missing}")

    # 若不提供預設值，不存在的屬性回傳 None
    none_val: Optional[str] = root.get("no_such_attr")
    print(f"不存在的屬性（無預設值）：{none_val}")


# ════════════════════════════════════════════════════════════
#  5. 建立 XML 與寫入檔案（ET.SubElement / ET.ElementTree）
#  手動建立 XML 的步驟：
#    1. ET.Element("tag", attrib)   → 建立根元素
#    2. ET.SubElement(parent, "tag", attrib) → 建立子元素
#    3. elem.text = "..."           → 設定文字內容
#    4. ET.ElementTree(root)        → 建立 ElementTree 物件
#    5. tree.write(file, ...)       → 寫入檔案
# ════════════════════════════════════════════════════════════

def demo_create_xml() -> None:
    """
    使用 Element 與 SubElement 建立 XML 樹，並寫入檔案。

    ET.Element(tag, attrib=None)：
      - 建立一個新的元素節點
      - tag：標籤名稱（str）
      - attrib：屬性字典（可選）

    ET.SubElement(parent, tag, attrib=None)：
      - 在 parent 底下建立子元素
      - 回傳新建的子元素

    ET.ElementTree(root)：
      - 以 root 為根建立 ElementTree 物件
      - tree.write(file, encoding, xml_declaration) 寫入檔案
    """
    print("\n=== 建立 XML（Element / SubElement）===")

    # 建立根元素 <students>
    root: ET.Element = ET.Element("students")

    # 建立第一個學生 <student id="1">
    s1: ET.Element = ET.SubElement(root, "student", attrib={"id": "1"})
    name1: ET.Element = ET.SubElement(s1, "name")
    name1.text = "Alice"
    score1: ET.Element = ET.SubElement(s1, "score")
    score1.text = "90"

    # 建立第二個學生 <student id="2">
    s2: ET.Element = ET.SubElement(root, "student", attrib={"id": "2"})
    name2: ET.Element = ET.SubElement(s2, "name")
    name2.text = "Bob"
    score2: ET.Element = ET.SubElement(s2, "score")
    score2.text = "85"

    # 建立 ElementTree 並寫入檔案
    tree: ET.ElementTree = ET.ElementTree(root)
    filepath: str = "/tmp/students.xml"
    tree.write(filepath, encoding="utf-8", xml_declaration=True)

    print(f"已寫入檔案：{filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        print(f"內容：\n{f.read()}")


# ════════════════════════════════════════════════════════════
#  6. 從檔案解析（ET.parse）
#  ET.parse(filepath) → 回傳 ElementTree 物件
#  tree.getroot()     → 取得根 Element
#
#  實務上最常用的是從檔案讀取 XML，而非從字串解析。
# ════════════════════════════════════════════════════════════

def demo_parse_file() -> None:
    """
    使用 ET.parse() 從檔案讀取 XML 並解析。

    ET.parse(filepath)：
      - 開啟檔案、讀取內容、解析為 ElementTree
      - 回傳 ElementTree 物件
      - 檔案不存在會拋出 FileNotFoundError

    tree.getroot()：
      - 回傳根元素的 Element 物件
      - 之後即可使用 find / findall / iter / get 等方法操作
    """
    print("\n=== 從檔案解析（ET.parse）===")

    filepath: str = "/tmp/students.xml"

    try:
        # ET.parse 會自動處理檔案開啟與解析
        tree: ET.ElementTree = ET.parse(filepath)
        root: ET.Element = tree.getroot()

        print(f"根標籤：{root.tag}")
        for student in root.findall("student"):
            sid: Optional[str] = student.get("id")
            name: Optional[str] = student.findtext("name")   # 便利方法
            score: Optional[str] = student.findtext("score")
            print(f"  學生 id={sid}：{name}，成績={score}")

    except FileNotFoundError:
        print(f"檔案 {filepath} 不存在，請先執行 demo_create_xml()")


# ════════════════════════════════════════════════════════════
#  7. 修改元素內容
#  直接對 Element 屬性賦值即可修改：
#    elem.text = "新文字"
#    elem.set("attr", "新值")
#    elem.append(new_child)   → 新增子元素
#    elem.remove(child)       → 移除子元素
# ════════════════════════════════════════════════════════════

def demo_modify_xml() -> None:
    """
    修改已存在的 XML 元素（修改文字、屬性、新增/刪除子元素）。

    常用修改方法：
      elem.text = "新文字"       → 修改文字內容
      elem.set("attr", "值")     → 修改/新增屬性
      elem.append(child)         → 新增子元素
      elem.remove(child)         → 刪除子元素
      elem.clear()               → 清空所有子元素與屬性
    """
    print("\n=== 修改 XML ===")

    # 先從字串解析一個簡單 XML 來修改
    xml_str: str = "<book><title>原始書名</title><price>300</price></book>"
    root: ET.Element = ET.fromstring(xml_str)

    print(f"修改前：{ET.tostring(root, encoding='unicode')}")

    # 修改文字
    title: Optional[ET.Element] = root.find("title")
    if title is not None:
        title.text = "新書名"

    # 修改屬性
    root.set("updated", "yes")

    # 新增子元素
    author: ET.Element = ET.SubElement(root, "author")
    author.text = "王小明"

    # 刪除子元素
    price: Optional[ET.Element] = root.find("price")
    if price is not None:
        root.remove(price)

    print(f"修改後：{ET.tostring(root, encoding='unicode')}")


# ════════════════════════════════════════════════════════════
#  主程式：依序執行各示範函式
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    root: ET.Element = demo_parse_and_basics(RAW_XML)
    demo_find_findall(root)
    demo_iter(root)
    demo_get_attributes(root)
    demo_create_xml()
    demo_parse_file()
    demo_modify_xml()
