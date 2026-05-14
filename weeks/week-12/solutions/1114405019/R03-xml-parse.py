# R03-xml-parse.py
# 使用 xml.etree.ElementTree 進行 XML 解析與節點操作

import xml.etree.ElementTree as ET

def xml_demo():
    # 建立 XML 字串
    xml_data = """
    <library>
        <book id="1">
            <title>Python 101</title>
            <author>John Doe</author>
        </book>
        <book id="2">
            <title>Algorithms</title>
            <author>Jane Smith</author>
        </book>
    </library>
    """

    # 解析 XML
    root = ET.fromstring(xml_data)
    print(f"根節點標籤: {root.tag}")

    # 遍歷節點
    print("\n--- 遍歷書籍 ---")
    for book in root.findall('book'):
        book_id = book.get('id')
        title = book.find('title').text
        author = book.find('author').text
        print(f"ID: {book_id}, 書名: {title}, 作者: {author}")

    # 修改節點: 新增一本書
    new_book = ET.SubElement(root, "book", {"id": "3"})
    ET.SubElement(new_book, "title").text = "Data Science"
    ET.SubElement(new_book, "author").text = "Lee"

    print("\n--- 新增節點後遍歷所有標題 ---")
    for title in root.iter('title'):
        print(f"書名: {title.text}")

if __name__ == "__main__":
    print("=== XML 解析示範 ===")
    xml_demo()
