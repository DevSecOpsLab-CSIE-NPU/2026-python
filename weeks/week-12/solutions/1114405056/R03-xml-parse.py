"""R03: xml.etree.ElementTree parse basics."""

import xml.etree.ElementTree as ET

xml_data = """
<rss version="2.0">
  <channel>
    <title>Planet Python</title>
    <item>
      <title>Typing Tips</title>
      <link>https://example.com/1</link>
      <author>Alice</author>
    </item>
    <item>
      <title>Asyncio Best Practices</title>
      <link>https://example.com/2</link>
      <author>Bob</author>
    </item>
  </channel>
</rss>
"""

root = ET.fromstring(xml_data)
print("root:", root.tag)
print("attrs:", root.attrib)

channel = root.find("channel")
print("channel title:", channel.find("title").text)

for item in root.findall("channel/item"):
    title = item.find("title").text
    author = item.find("author").text
    print(f"[{author}] {title}")

print("\nall <title>:")
for elem in root.iter("title"):
    print(" ", elem.text)

version = root.get("version")
print("\nversion:", version)
print("missing attr:", root.get("missing", "default"))
