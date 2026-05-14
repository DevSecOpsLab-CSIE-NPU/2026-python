"""R03 XML 解析詳細註解版。"""

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


def main():
    # fromstring 會把 XML 字串變成樹狀結構，
    # root 就是最外層的節點 <rss>。
    root = ET.fromstring(XML_DATA)

    # tag 代表標籤名稱，get() 代表讀取屬性值。
    print(root.tag, root.get("version"))

    # find("channel") 找到第一個 <channel> 節點。
    channel = root.find("channel")

    # findtext("title") 可以直接取出子節點文字。
    print(channel.findtext("title"))

    # findall("channel/item") 會找出所有 item。
    for item in root.findall("channel/item"):
        print(item.findtext("author"), item.findtext("title"))


if __name__ == "__main__":
    main()
