"""R03 XML 解析簡化版。"""

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
    root = ET.fromstring(XML_DATA)
    print(root.tag, root.get("version"))

    channel = root.find("channel")
    print(channel.findtext("title"))

    for item in root.findall("channel/item"):
        print(item.findtext("author"), item.findtext("title"))


if __name__ == "__main__":
    main()
