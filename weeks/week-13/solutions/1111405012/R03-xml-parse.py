"""R03. XML 解析基礎（6.3）"""

from __future__ import annotations

import xml.etree.ElementTree as ET


XML_DATA = """
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


def parse_xml(xml_text: str) -> ET.Element:
    """把 XML 字串解析成根節點。"""
    return ET.fromstring(xml_text)


def get_child_text(element: ET.Element, child_tag: str) -> str:
    """安全取得子節點文字，找不到時回傳空字串。"""
    child = element.find(child_tag)
    return child.text if child is not None and child.text is not None else ""


def get_channel_title(root: ET.Element) -> str:
    """取得 channel/title 文字。"""
    channel = root.find("channel")
    if channel is None:
        return ""
    return get_child_text(channel, "title")


def list_items(root: ET.Element) -> list[dict[str, str]]:
    """列出所有 item 的 title、link、author。"""
    items: list[dict[str, str]] = []
    for item in root.findall("channel/item"):
        items.append(
            {
                "title": get_child_text(item, "title"),
                "link": get_child_text(item, "link"),
                "author": get_child_text(item, "author"),
            }
        )
    return items


def list_titles(root: ET.Element) -> list[str]:
    """用 iter 收集所有 title 標籤的文字。"""
    return [element.text or "" for element in root.iter("title")]


def get_attribute(element: ET.Element, name: str, default: str | None = None) -> str | None:
    """讀取屬性，若不存在則回傳預設值。"""
    return element.get(name, default)


def main() -> None:
    """印出課堂上示範的 XML 解析結果。"""
    root = parse_xml(XML_DATA)
    print("根標籤：", root.tag)
    print("屬性：", root.attrib)
    print("頻道名稱：", get_channel_title(root))

    for item in list_items(root):
        print(f"  [{item['author']}] {item['title']}")

    print("\n所有 <title>：")
    for title in list_titles(root):
        print(" ", title)

    print("\nRSS 版本：", get_attribute(root, "version"))
    print("不存在的屬性：", get_attribute(root, "missing", "預設值"))


if __name__ == "__main__":
    main()
