# AI 使用紀錄

1. **你問了哪些問題**
   - Python 如何寫一個簡單的 Decorator 來算執行時間並列印出來。
   - 如何將 ElementTree (`ET`) 儲存為帶有換行的漂亮 XML (`pretty_xml`) 格式。
   - Python 裡面用什麼方式畫長條圖並在上面貼上數字標籤。
   - Python 的 unittest 要怎麼進行空值（Empty List）邊界條件的驗證。

2. **AI 建議你有採用的部分**
   - 採用 `xml.dom.minidom` 把 `ET.tostring` 回傳的值再次解析來產生格式化漂亮（有縮排）的 XML。
   - 採用 `.get()` 代替原本如果缺少 KeyError 的字典抓取方法，以免除不必要的意外崩潰。
   - 採用 `unittest.TestCase` 中簡潔的 `self.assertEqual` 寫法並建立 TestCase 類別骨架。

3. **AI 建議你拒絕的部分及原因**
   - AI 給予了複雜的 lxml 第三方函式庫去渲染 XML。原因：考量作業不應無端依賴外部庫，故我選擇了標準庫裡的 `minidom`。
   - AI 原本建議圖表記錄時間包含四個位數即可。原因：以這份程式來講執行都太快了不到 0.001 秒，如果不保留六個有效位數可能會顯示 0.0000 造成無法比較的問題。

4. **1 個「AI 輸出你執行後發現有誤」的案例與修正過程**
   - **錯誤**: AI 會把 `matplotlib.pyplot.text(bar.get_x(), bar.get_height(), ...)` 作為標籤置中的作法。
   - **修正**: x 軸的起底不是真正中心，實際執行會偏左跑版。我把寫法修改為 `bar.get_x() + bar.get_width()/2`，最後搭配 `ha='center'` 成功在圖形的頭頂正中央顯示了漂亮的時間文字。