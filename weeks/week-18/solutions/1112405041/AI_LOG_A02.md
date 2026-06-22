# AI_LOG - A02 凱撒密碼

## 我問 AI 什麼

> 逐字貼上我實際輸入的提示詞：
慢慢拆解我的 問題 !!!!  我有符合情境? 情境 SCENARIO
這是一場 CPE 模擬實戰：題目分 A / B / C 三區，難度與分數遞增。規則照平時練的來——每一題用 TDD + Git PR SOP 交卷：開分支 → 先寫測試 (紅燈) commit → 再寫實作 (綠燈) commit → push → 開 PR (你的 fork 分支 → 課程 repo main) → PR 附 AI_LOG.md。 可翻書、可上網、可用 AI，但時間會被吃掉，勝負在熟練度。先拿 A 區保底，再往 B、C 推進。(我的第一題 有嗎?)第二題 凱撒密碼 (Caesar Cipher) [ A 區 · 保底 ] [ 25 分 ]

步驟②「再拿一塊保底」：用古典凱撒位移加密一段文字。本題為 W3 字串處理題型。

相關教材 (可參考)：weeks/week-08/QUESTION-10222.md (鍵盤右移位移密碼，本題原型)、week-03/README.md (字串加密與頻率)。
! 用 AI 前先回答首頁五項檢查表 (簽名 / 邊界 / 例外 / edge case / 驗收)，填滿才開始協作。

～ 一、題目敘述
將每行字串中的英文字母向後位移 SHIFT 位 (SHIFT 依學號個位，見參數頁 我是 位移 SHIFT=2 )：大寫在 A~Z 內循環、小寫在 a~z 內循環 (例如 SHIFT=3 時 z→c、Y→B)；非英文字母字元 (空白、數字、標點) 原樣保留。

～ 二、輸入說明
輸入包含多行，每行一個字串 (可能含空白、標點，長度 ≤ 1000)，讀到檔案結尾 (EOF) 為止。

～ 三、輸出說明
對每一行輸入，輸出加密後的字串 (一行對一行)。

～ 四、範例 (Sample, 假設 SHIFT = 3)
Sample Input

Hello, NPU!
abc XYZ
Sample Output

Khoor, QSX!
def ABC
H→K, e→h, l→o, o→r；逗號、空白、驚嘆號不變。X→A, Y→B, Z→C 循環回開頭。

∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出
我的位移 SHIFT = 2 (個位 u → u%25+1 )
用你的 SHIFT 重算上面 Sample Input 的輸出 (兩行)：
Hello, NPU! → ______________________
abc XYZ     → ______________________

驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。



回 main 開新分支（建議）： 第二題 做 A02



所以第二題 你跟我說要做 甚麼 ?(還有要用老師　ＡＧＥＮＴ．ＭＤ


～ 三、輸出說明 對每一行輸入，輸出加密後的字串 (一行對一行)。
～ 四、範例 (Sample, 假設 SHIFT = 3) Sample Input
Hello, NPU!
abc XYZ
Sample Output
Khoor, QSX!
def ABC
H→K, e→h, l→o, o→r；逗號、空白、驚嘆號不變。X→A, Y→B, Z→C 循環回開頭。
∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出 我的位移 SHIFT = 2 (個位 u → u%25+1 ) 用你的 SHIFT 重算上面 Sample Input 的輸出 (兩行)： Hello, NPU! → ______________________ abc XYZ → ______________________
驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。 國立澎湖科技大學 資訊工程系 趙達毅 第 4 / 6 頁



慢慢拆解我的 問題 !!!!  我有符合情境? 情境 SCENARIO
這是一場 CPE 模擬實戰：題目分 A / B / C 三區，難度與分數遞增。規則照平時練的來——每一題用 TDD + Git PR SOP 交卷：開分支 → 先寫測試 (紅燈) commit → 再寫實作 (綠燈) commit → push → 開 PR (你的 fork 分支 → 課程 repo main) → PR 附 AI_LOG.md。 可翻書、可上網、可用 AI，但時間會被吃掉，勝負在熟練度。先拿 A 區保底，再往 B、C 推進。(我的第一題 有嗎?)第二題 凱撒密碼 (Caesar Cipher) [ A 區 · 保底 ] [ 25 分 ]

步驟②「再拿一塊保底」：用古典凱撒位移加密一段文字。本題為 W3 字串處理題型。

相關教材 (可參考)：weeks/week-08/QUESTION-10222.md (鍵盤右移位移密碼，本題原型)、week-03/README.md (字串加密與頻率)。
! 用 AI 前先回答首頁五項檢查表 (簽名 / 邊界 / 例外 / edge case / 驗收)，填滿才開始協作。

～ 一、題目敘述
將每行字串中的英文字母向後位移 SHIFT 位 (SHIFT 依學號個位，見參數頁 我是 位移 SHIFT=2 )：大寫在 A~Z 內循環、小寫在 a~z 內循環 (例如 SHIFT=3 時 z→c、Y→B)；非英文字母字元 (空白、數字、標點) 原樣保留。

～ 二、輸入說明
輸入包含多行，每行一個字串 (可能含空白、標點，長度 ≤ 1000)，讀到檔案結尾 (EOF) 為止。

～ 三、輸出說明
對每一行輸入，輸出加密後的字串 (一行對一行)。

～ 四、範例 (Sample, 假設 SHIFT = 3)
Sample Input

Hello, NPU!
abc XYZ
Sample Output

Khoor, QSX!
def ABC
H→K, e→h, l→o, o→r；逗號、空白、驚嘆號不變。X→A, Y→B, Z→C 循環回開頭。

∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出
我的位移 SHIFT = 2 (個位 u → u%25+1 )
用你的 SHIFT 重算上面 Sample Input 的輸出 (兩行)：
Hello, NPU! → ______________________
abc XYZ     → ______________________

驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。



回 main 開新分支（建議）： 第二題 做 A02



所以第二題 你跟我說要做 甚麼 ?(還有要用老師　ＡＧＥＮＴ．ＭＤ


～ 三、輸出說明 對每一行輸入，輸出加密後的字串 (一行對一行)。
～ 四、範例 (Sample, 假設 SHIFT = 3) Sample Input
Hello, NPU!
abc XYZ
Sample Output
Khoor, QSX!
def ABC
H→K, e→h, l→o, o→r；逗號、空白、驚嘆號不變。X→A, Y→B, Z→C 循環回開頭。
∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出 我的位移 SHIFT = 2 (個位 u → u%25+1 ) 用你的 SHIFT 重算上面 Sample Input 的輸出 (兩行)： Hello, NPU! → ______________________ abc XYZ → ______________________
驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。 國立澎湖科技大學 資訊工程系 趙達毅 第 4 / 6 頁



Ａ０２　根據　ＡＧＥＮＴ　.MD 你先教學 1-5 階段要問 甚麼 再開始 詢問我 順便 給我你想要怎麼設計 甚麼 然後根據題目 要求 設計 我看 再來 採用  慢慢拆解我的 問題 !!!!  我有符合情境? 情境 SCENARIO
這是一場 CPE 模擬實戰：題目分 A / B / C 三區，難度與分數遞增。規則照平時練的來——每一題用 TDD + Git PR SOP 交卷：開分支 → 先寫測試 (紅燈) commit → 再寫實作 (綠燈) commit → push → 開 PR (你的 fork 分支 → 課程 repo main) → PR 附 AI_LOG.md。 可翻書、可上網、可用 AI，但時間會被吃掉，勝負在熟練度。先拿 A 區保底，再往 B、C 推進。(我的第一題 有嗎?)第二題 凱撒密碼 (Caesar Cipher) [ A 區 · 保底 ] [ 25 分 ]

步驟②「再拿一塊保底」：用古典凱撒位移加密一段文字。本題為 W3 字串處理題型。

相關教材 (可參考)：weeks/week-08/QUESTION-10222.md (鍵盤右移位移密碼，本題原型)、week-03/README.md (字串加密與頻率)。
! 用 AI 前先回答首頁五項檢查表 (簽名 / 邊界 / 例外 / edge case / 驗收)，填滿才開始協作。

～ 一、題目敘述
將每行字串中的英文字母向後位移 SHIFT 位 (SHIFT 依學號個位，見參數頁 我是 位移 SHIFT=2 )：大寫在 A~Z 內循環、小寫在 a~z 內循環 (例如 SHIFT=3 時 z→c、Y→B)；非英文字母字元 (空白、數字、標點) 原樣保留。

～ 二、輸入說明
輸入包含多行，每行一個字串 (可能含空白、標點，長度 ≤ 1000)，讀到檔案結尾 (EOF) 為止。

～ 三、輸出說明
對每一行輸入，輸出加密後的字串 (一行對一行)。

～ 四、範例 (Sample, 假設 SHIFT = 3)
Sample Input

Hello, NPU!
abc XYZ
Sample Output

Khoor, QSX!
def ABC
H→K, e→h, l→o, o→r；逗號、空白、驚嘆號不變。X→A, Y→B, Z→C 循環回開頭。

∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出
我的位移 SHIFT = 2 (個位 u → u%25+1 )
用你的 SHIFT 重算上面 Sample Input 的輸出 (兩行)：
Hello, NPU! → ______________________
abc XYZ     → ______________________

驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。



回 main 開新分支（建議）： 第二題 做 A02



所以第二題 你跟我說要做 甚麼 ?(還有要用老師　ＡＧＥＮＴ．ＭＤ


～ 三、輸出說明 對每一行輸入，輸出加密後的字串 (一行對一行)。
～ 四、範例 (Sample, 假設 SHIFT = 3) Sample Input
Hello, NPU!
abc XYZ
Sample Output
Khoor, QSX!
def ABC
H→K, e→h, l→o, o→r；逗號、空白、驚嘆號不變。X→A, Y→B, Z→C 循環回開頭。
∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出 我的位移 SHIFT = 2 (個位 u → u%25+1 ) 用你的 SHIFT 重算上面 Sample Input 的輸出 (兩行)： Hello, NPU! → ______________________ abc XYZ → ______________________
驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。 國立澎湖科技大學 資訊工程系 趙達毅 第 4 / 6 頁


你覺得這個設計可以嗎？你確認後我開始問你檢查表的答案，然後出測試 code。 我覺得很棒 問之前 題目 要洩題給我 再給我答案


我符合 老師的 SAMPLE INPUT 的 預期輸出? 跟 SAMPLE OUT PUT?


函式名稱：caesar_encrypt
參數：text: str (要加密的字串), shift: int (位移量)
回傳：str (加密後的字串) 每行長度	≤ 1000 字元
讀取方式	for line in sys.stdin 讀到 EOF
結束條件	EOF（沒有固定行數） 情況	處理方式
空行	直接 print() 輸出空行（保留行數對齊）
非英文字母	原樣保留，不做任何處理 #	Edge case	案例 SHIFT=2	預期輸出	陷阱
1	大寫繞圈	XYZ	ZAB	Y(89)+2=91→65(A), Z(90)+2=92→66(B)
2	小寫繞圈	xyz	zab	y(121)+2=123→97(a), z(122)+2=124→98(b)
3	非字母不動	123 !@#	123 !@#	數字、空白、標點全部保留
4	空字串	""	""	迴圈跑 0 次，回傳空字串  驗收標準 — 預期答案
你的 SHIFT = 2

Sample Input:          Sample Output (SHIFT=2):
Hello, NPU!     →      Jgnnq, NRW!
abc XYZ         →      cde ZAB


先給我 POWER SHELL 第二題執行紅燈測試

OK 繼續

做好了 紅燈

我該怎麼 驗算程式 直接開 TEST CASE?   或手動 輸入 ?新增 AI LOG.MD 翻本 ( LOOK WEEK 15 16 17 FOLDER ) 幫我查 (並補正至 A02

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041> Write-Output "Hello, NPU!" "abc XYZ" | python weeks\week-18\solutions\1112405041\A02.py
C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe: can't open file 'C:\\Users\\User\\Downloads\\20260622clip\\2026-python\\weeks\\week-18\\solutions\\1112405041\\weeks\\week-18\\solutions\\1112405041\\A02.py': [Errno 2] No such file or directory
PS C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041>  (我要測試!!!!


去開PR 你的 路徑 要怎麼 開?



摘要
1. 分析 week 15 16 17 全部檔案 跟 AGENT.MD 重點是？考試要準備什麼？
2. 第二題 凱撒密碼，將每行英文字母向後位移 SHIFT=2，大寫 A~Z 循環、小寫 a~z 循環，非字母不動。請先教學檢查表 1-5 再回答。
3. 根據 ✅簽名 ✅邊界 ✅例外 ✅Edge ✅驗收 逐一測試，教我使用 powershell 執行紅燈綠燈。
4. 幫我產出 A02.py 的測試 stub 與實作 code。請先給測試（紅燈），我 commit 後再給實作（綠燈）。


## AI 給了什麼

> AI 回應重點：

1. 先教學 5 項檢查表的原理與預期答案，並給出他的設計方案（`caesar_encrypt(text, shift)`，用 ord/chr + %26 做循環位移）
2. 我確認採用設計後，AI 給 `test_A02.py` 共 8 個測試案例（基本、大寫繞圈、小寫繞圈、非字母不變、空字串、混合大小寫、全部字母循環、主程式多行輸出）
3. 給我 stub 框架跑紅燈 → 我 commit `test:` 後 → 給實作 code 轉綠燈
4. 發現測試預期值寫錯（NPU→NRW 應為 NPU→PRW），修正後 8/8 OK

## 我改了什麼

> AI 給的測試中 `test_basic_case` 預期值是 `Jgnnq, NRW!`，但我手動驗算 N+2=P、P+2=R、U+2=W，正確應為 `Jgnnq, PRW!`。回報 AI 後修正測試預期值，8 題全綠。

我手動測試 發現 輸入 不同有不同 結果 為可以 用的 程式


## AI 反問我什麼 / 我怎麼回答

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 函式簽名叫什麼？參數與回傳？ | `caesar_encrypt(text: str, shift: int) -> str` |
| SHIFT 值怎麼算？ | 學號個位數 1 → 1%25+1 = 2 |
| 空行怎麼處理？ | print() 輸出空行，保留行數對齊 |
| 非英文字母怎麼處理？ | 原樣保留，不做任何處理 |
| edge case 要測哪些？ | 大寫繞圈、小寫繞圈、非字母不動、空字串 |
