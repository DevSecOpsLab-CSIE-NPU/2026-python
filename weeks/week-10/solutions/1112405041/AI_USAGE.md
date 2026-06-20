1. 你問了哪些問題（條列 3–5 條）
   - read_csv 裡檔案不存在時應該主動接還是讓 Python 拋錯？
   - count_by_dept 遇到空字串科系該怎麼算？
   - build_xml_tree 從 dict 建 XML 的標準做法？
   - 安全掃描的 OpenSSF 規則要檢查哪些項目？

2. AI 建議你有採用的部分
   - count_by_dept 加入 type annotation 和 is not None 檢查（取代 if dept: 的 falsy 判斷）
   - import os 搬到檔案最上方（符合 PEP8 及 OpenSSF 08 規則）
   - write_xml 用 xml.etree.ElementTree 搭配 tree.write 輸出

3. AI 建議你拒絕的部分及原因
   - AI 提議在 read_csv 裡自訂 FileNotFoundError 訊息包裝（拒絕，因為讓 Python 自然拋出反而更簡潔，也符合助教範例風格）

4. 至少 1 個「AI 輸出你執行後發現有誤」的案例與修正過程
   - AI 第一次給的 build_xml_tree 假設 data 是 {"students": [...]} 的 dict，但實際上 read_json 回傳的是純 list。執行後 AttributeError，我把 tree root 改為直接從傳入的 list iter 建立 student 子節點就正常了。
