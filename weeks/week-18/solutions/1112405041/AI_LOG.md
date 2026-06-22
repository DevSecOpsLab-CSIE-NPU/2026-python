# AI_LOG - A01 資料清理

## 我問 AI 什麼

> 逐字貼上我實際輸入的提示詞：
分析week 15 16 17 全部檔案 跟 AGENT.MD 重點是 ? 考試 要準備甚麼 呢?
大概全流程 是 長怎樣? 考試要預備 甚麼 呢?
在week18 > solution > 開1112405041 folder
新增A01 python 檔案 並參考 week02 HOMEWORK.MD (開始考試了) week-02 bloom-examples/ R10-dedupe.py r09 -dict-set.py 你先讀 一下 實際做不同的 內容
整除數D 位移SHIFT  2 進位基底 BASE =8 搜尋目標K=141 ✔	評分項目	配分	得分
第一題 (A 區) 資料清理 30 分			
□	輸出正確 (多組測資、依學號整除數 D、含 edge case)	22	
□	Git PR SOP 完整 (分支 / 先紅後綠 / PR base, compare / 描述三要件) + AI_LOG.md	8 情境 SCENARIO這是一場 CPE 模擬實戰：題目分 A / B / C 三區，難度與分數遞增。規則照平時練的來——每一題用 TDD + Git PR SOP 交卷：開分支 → 先寫測試 (紅燈) commit → 再寫實作 (綠燈) commit → push → 開 PR (你的 fork 分支 → 課程 repo main) → PR 附 AI_LOG.md。 可翻書、可上網、可用 AI，但時間會被吃掉，勝負在熟練度。先拿 A 區保底，再往 B、C 推進。～ AI 協作協議 (作答前必讀)本卷可用 AI 協作，但不提供任何範例程式與提示詞，要問什麼、怎麼問自己想。最重要的規則：你必須先回答下方「開工前資訊檢查表」，AI 才能開始幫你產出程式。檢查表沒填滿就先要 code，視為違反協議——請在 AI_LOG.md 逐字記錄「AI 反問我什麼 / 我怎麼回答」，這是你沒有放空、是你在主導的證據。每題開工前先回答你要先想清楚並寫進對話 / AI_LOG.md 的事① 函式簽名函式叫什麼？吃什麼參數、回傳什麼型別？② 輸入邊界資料範圍、筆數上限、輸入到 EOF 還是讀固定行數？③ 例外處理非法輸入 / 空輸入 / 格式錯誤要怎麼處理？④ edge case至少列出 1 個邊界案例 (如 0、空集合、全部被剔除、剛好等於門檻)。⑤ 驗收標準什麼樣的輸出才算對？依你學號的參數值是多少？流程不變：先測試 (紅燈) → commit → 再實作 (綠燈) → commit。AI 給你的東西要自己手打、自己測、自己負責。流程相關教材 (可參考)：weeks/week-15/in_class/exam-sop-checklist-lite.md (8 步驟 SOP)、ai-log-template.md (AI_LOG 範本)、week-16/README.md (分數結構)。完整複習索引：weeks/week-18/STUDY_GUIDE.md。國立澎湖科技大學 資訊工程系 第 1 / 6 頁
題目 還沒 設計完  第一題 資料清理 (Data Cleaning) [ A 區 · 保底 ] [ 30 分 ]

步驟①「拿保底」：一份整數資料常有重複與雜訊，請把它清乾淨。本題為學期初已練過的序列 / 字典題型。

相關教材 (可參考)：weeks/week-02/HOMEWORK.md (序列清理)、week-02/bloom-examples/R10-dedupe.py (去重保存)、R09-dict-sets.py。
! 用 AI 前先回答首頁五項檢查表 (簽名 / 邊界 / 例外 / edge case / 驗收)，填滿才開始協作。

～ 一、題目敘述
對每一組整數數列，依序完成三步：①去除重複 (保留第一次出現的順序) → ②只保留能被 D 整除的數 (D 依學號個位，見參數頁) → ③由小到大排序。

～ 二、輸入說明
輸入包含多組測資。每組第一行一個整數 n (1 ≤ n ≤ 10⁵)，表示數列長度；第二行有 n 個以空白分隔的整數 (-10⁹ ≤ a_i ≤ 10⁹)。
當某組的 n = 0 時代表輸入結束，該組不需處理。

～ 三、輸出說明
對每組測資輸出一行：處理後的數列，數字間以單一空白分隔；若沒有任何數字符合，該行輸出 NONE。

～ 四、範例 (Sample, 假設 D = 2)
Sample Input

8
4 7 4 2 9 2 6 7
3
1 3 5
0
Sample Output

2 4 6
NONE
第 1 組：去重保序 → 4 7 2 9 6；能被 2 整除 → 4 2 6；升冪 → 2 4 6。第 2 組無偶數 → NONE。

∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出
我的整除數 D = 3 (個位 u → u%4+2 )
用你的 D 重算上面 Sample Input 的輸出 (兩組)：
第 1 組：______________________
第 2 組：______________________

驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。
你先告訴我第一題打算怎麼 設計?
這個 設計 符合題目 跟預期 輸出結果?
掛入 AGENT.MD (外面的 不然 17 週 的  有問題 的 話 要 可以 脫離 情境
這次考試要觸發喔
掛入 AGENT.MD (外面的 不然 17 週 的  有問題 的 話 要 可以 脫離 情境   這次考試要觸發喔  都不用問問題?  ～ AI 協作協議 (作答前必讀)本卷可用 AI 協作，但不提供任何範例程式與提示詞，要問什麼、怎麼問自己想。最重要的規則：你必須先回答下方「開工前資訊檢查表」，AI 才能開始幫你產出程式。檢查表沒填滿就先要 code，視為違反協議——請在 AI_LOG.md 逐字記錄「AI 反問我什麼 / 我怎麼回答」，這是你沒有放空、是你在主導的證據。每題開工前先回答你要先想清楚並寫進對話 / AI_LOG.md 的事① 函式簽名函式叫什麼？吃什麼參數、回傳什麼型別？② 輸入邊界資料範圍、筆數上限、輸入到 EOF 還是讀固定行數？③ 例外處理非法輸入 / 空輸入 / 格式錯誤要怎麼處理？④ edge case至少列出 1 個邊界案例 (如 0、空集合、全部被剔除、剛好等於門檻)。⑤ 驗收標準什麼樣的輸出才算對？依你學號的參數值是多少？
還有記得 要掛入老師 標準的 才有情境 另外 為了 符合 教學用途 你要先告訴 我 1-5 答案 原理 才可以 問我  掛入 AGENT.MD (外面的 不然 17 週 的  有問題 的 話 要 可以 脫離 情境   這次考試要觸發喔  都不用問問題?  ～ AI 協作協議 (作答前必讀)本卷可用 AI 協作，但不提供任何範例程式與提示詞，要問什麼、怎麼問自己想。最重要的規則：你必須先回答下方「開工前資訊檢查表」，AI 才能開始幫你產出程式。檢查表沒填滿就先要 code，視為違反協議——請在 AI_LOG.md 逐字記錄「AI 反問我什麼 / 我怎麼回答」，這是你沒有放空、是你在主導的證據。每題開工前先回答你要先想清楚並寫進對話 / AI_LOG.md 的事① 函式簽名函式叫什麼？吃什麼參數、回傳什麼型別？② 輸入邊界資料範圍、筆數上限、輸入到 EOF 還是讀固定行數？③ 例外處理非法輸入 / 空輸入 / 格式錯誤要怎麼處理？④ edge case至少列出 1 個邊界案例 (如 0、空集合、全部被剔除、剛好等於門檻)。⑤ 驗收標準什麼樣的輸出才算對？依你學號的參數值是多少？
為了 符合 教學用途 你要先告訴 我 1-5 答案 原理 才可以 問我  為了 符合 教學用途 你要先告訴 我 1-5 答案 原理 才可以 問我 ① 函式簽名

函式名稱你打算叫什麼？
參數有幾個？分別是什麼型別？
回傳什麼型別？
② 輸入邊界

n 的範圍？
整數值的範圍？
遇到 n=0 是做什麼？
③ 例外處理

輸入格式錯誤或空行要怎麼處理？
當沒有任何數字留下時，輸出什麼？回傳空 list 還是特別處理？
④ Edge case

至少舉 1 個你覺得最容易錯的邊界情況
⑤ 驗收標準

Sample Input 用你的 D 跑出來長怎樣？第一組輸出什麼？第二組輸出什麼？

現在我懂了 你打算讓我回答?


每題開工前先回答你要先想清楚並寫進對話 / AI_LOG.md 的事① 函式簽名函式叫什麼？吃什麼參數、回傳什麼型別？② 輸入邊界資料範圍、筆數上限、輸入到 EOF 還是讀固定行數？③ 例外處理非法輸入 / 空輸入 / 格式錯誤要怎麼處理？④ edge case至少列出 1 個邊界案例 (如 0、空集合、全部被剔除、剛好等於門檻)。⑤ 驗收標準什麼樣的輸出才算對？依你學號的參數值是多少？ (我的 1  題目要做三件事：去重 → 整除篩選 → 升冪排序。

所以函式的「核心邏輯」應該是吃一個整數 list + D，回傳處理後的 list。主程式負責 stdin 讀多組。

預期答案長這樣：

函式名稱：clean_data 或 process_cleaning
參數：nums: list[int], D: int
回傳：list[int]（空結果回傳空 list []，由主程式判斷輸出 NONE）
為什麼這樣設計？

把「處理邏輯」跟「IO 讀取」分開 → 測試時只要測 clean_data(...)，不用真的從 stdin 讀 
回傳 list[int] 比回傳字串更通用，要轉成輸出字串是主程式的事( 我覺得 你的 思考挺有道理 採用) Sample Input 用 D=3 跑： (這符合輸入邊界了?) 例外處理 非法輸入 / 空輸入 / 格式錯誤要怎麼處理？ (請你教學 我 懂了 我再回答)  edge case  至少列出 1 個邊界案例 (如 0、空集合、全部被剔除、剛好等於門檻)。  (請你教學 我 懂了 我再回答)  驗收標準  什麼樣的輸出才算對？依你學號的參數值是多少？ (你還記得?)(請重新教學　）　我看是這樣　才對　Sample Input 用 D=3 跑：

第 1 組：4 7 4 2 9 2 6 7

步驟	過程	結果
① 去重保序	4 出現→留, 7→留, 4→跳, 2→留, 9→留, 2→跳, 6→留, 7→跳	[4, 7, 2, 9, 6]
② 除 3 篩選	4%3=1✗, 7%3=1✗, 2%3=2✗, 9%3=0✓, 6%3=0✓	[9, 6]
③ 升冪排序	小到大	[6, 9]
輸出		6 9
第 2 組：1 3 5

步驟	結果
① 去重保序	[1, 3, 5]
② 除 3 篩選	[3]（1%3=1✗, 3%3=0✓, 5%3=2✗）
③ 升冪排序	[3]
輸出	3

好，我重新教學③和④，等你說懂了再回答。

③ 例外處理 — 教學
本題的輸入是 CPE 標準格式： 每組第一行 n，第二行 n 個整數，n=0 結束。

常見的「非法/異常情況」有三種：

情況	怎麼處理	為什麼
空行（多按一個 Enter）	if not line: continue 跳過	CPE 測資偶爾會有空行，continue 最穩
n=0	break 直接結束	題目說 n=0 代表輸入結束
所有數字被篩光	回傳空 list []，主程式輸出 NONE	題目規定：沒有任何數字符合 → 輸出 NONE
不需要做的事：

不用檢查非整數輸入（題目保證格式正確）
不用 raise ValueError（題目沒要求）
不用處理負數 n（因為題目給 1 ≤ n ≤ 10⁵ 或 n=0）
執行順序：

輸入 n → n=0? → break
讀一行數字 → 拆成 list[int]
呼叫 clean_data(nums, D) → 拿結果
如果是 [] → 輸出 NONE
否則 → 輸出 " ".join(map(str, result))
④ Edge case — 教學
Edge case 是最容易錯但扣分最重的地方。這題至少要想 4 種：

#	Edge case	案例 (D=3)	預期輸出	陷阱在哪
1	全部被篩掉	3\n4 5 7	NONE	去重後 [4,5,7]，沒一個能被 3 整除 → 空 list，不能忘了 NONE
2	全部重複	5\n3 3 3 3 3	3	去重後只剩 [3]，整除後 [3]，不能輸出 3 3 3 3 3
3	單一元素且整除	1\n6	6	n=1 是最小合法輸入，要能正常處理
4	數字包含負數	4\n-6 -3 2 3	-6 -3 3	Python 的 -3 % 3 == 0，負數也能整除，不能漏掉
你現在要回答的（③ + ④）
③ 例外處理：

空行要怎麼處理？（continue / raise / 忽略？）
所有數字被篩光，clean_data 回傳什麼？主程式輸出什麼？
④ Edge case：

舉 1 個你覺得最容易忘記測的邊界情況
你懂了嗎？懂了就回答③和④，我確認後一起出測試 code。　（重看題目）　第一題 資料清理 (Data Cleaning) [ A 區 · 保底 ] [ 30 分 ]

步驟①「拿保底」：一份整數資料常有重複與雜訊，請把它清乾淨。本題為學期初已練過的序列 / 字典題型。

相關教材 (可參考)：weeks/week-02/HOMEWORK.md (序列清理)、week-02/bloom-examples/R10-dedupe.py (去重保存)、R09-dict-sets.py。
! 用 AI 前先回答首頁五項檢查表 (簽名 / 邊界 / 例外 / edge case / 驗收)，填滿才開始協作。

～ 一、題目敘述
對每一組整數數列，依序完成三步：①去除重複 (保留第一次出現的順序) → ②只保留能被 D 整除的數 (D 依學號個位，見參數頁) → ③由小到大排序。

～ 二、輸入說明
輸入包含多組測資。每組第一行一個整數 n (1 ≤ n ≤ 10⁵)，表示數列長度；第二行有 n 個以空白分隔的整數 (-10⁹ ≤ a_i ≤ 10⁹)。
當某組的 n = 0 時代表輸入結束，該組不需處理。

～ 三、輸出說明
對每組測資輸出一行：處理後的數列，數字間以單一空白分隔；若沒有任何數字符合，該行輸出 NONE。

～ 四、範例 (Sample, 假設 D = 2)
Sample Input

8
4 7 4 2 9 2 6 7
3
1 3 5
0
Sample Output

2 4 6
NONE
第 1 組：去重保序 → 4 7 2 9 6；能被 2 整除 → 4 2 6；升冪 → 2 4 6。第 2 組無偶數 → NONE。

∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出
我的整除數 D = 3 (個位 u → u%4+2 )
用你的 D 重算上面 Sample Input 的輸出 (兩組)：
第 1 組：______________________
第 2 組：______________________

驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。　（我已填寫好　預測Ｄ　根據你解釋）　～ 評分檢查表 (上機 demo / PR 驗收用，打成績用)✔評分項目配分得分第一題 (A 區) 資料清理 30 分□輸出正確 (多組測資、依學號整除數 D、含 edge case)22□Git PR SOP 完整 (分支 / 先紅後綠 / PR base, compare / 描述三要件) + AI_LOG.md8

空行（多按一個 Enter）	if not line: continue 跳過	CPE 測資偶爾會有空行，continue 最穩　所有數字被篩光	回傳空 list []，主程式輸出 NONE	題目規定：沒有任何數字符合 → 輸出 NONE　數字包含負數	4\n-6 -3 2 3	-6 -3 3	Python 的 -3 % 3 == 0，負數也能整除，不能漏掉　驗收標準（你已經會了，直接確認）

你的 D = 3（1 % 4 + 2）（真的是？
第 1 組輸出 6 9
第 2 組輸出 3



看１５　１６　１７　週　我需要繳交分支　的　ＰＲ？　（我能確保　我在ＭＡＩＮ　的　修改　可以　ＣＯＭＭＩＴ　到分支？
我在ＭＡＩＮ　上　
給我　ＰＯＷＥＲ　ＳＨＥＬＬ　ＣＯＭＭＭＡＮＤ
PS C:\Users\User\Downloads\20260622clip>  & 'C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe' 'c:\Users\User\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '53460' '--' 'C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py' 
EEEEEEEEEE
======================================================================
ERROR: test_all_duplicates (__main__.TestCleanData.test_all_duplicates)
全部重複 -> 只剩一個元素
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 21, in test_all_duplicates
    result = clean_data([3, 3, 3, 3, 3], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_basic_case (__main__.TestCleanData.test_basic_case)
基本案例：4 7 4 2 9 2 6 7 with D=3 -> [6, 9]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 11, in test_basic_case
    result = clean_data([4, 7, 4, 2, 9, 2, 6, 7], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_main_output_multi_group (__main__.TestCleanData.test_main_output_multi_group)
多組測資輸出
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 61, in test_main_output_multi_group
    main()
    ~~~~^^
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 15, in main
    result = clean_data(data, D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_main_output_none (__main__.TestCleanData.test_main_output_none)
主程式輸出 NONE 當空結果
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 53, in test_main_output_none
    main()
    ~~~~^^
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 15, in main
    result = clean_data(data, D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_mixed_with_duplicates (__main__.TestCleanData.test_mixed_with_duplicates)
混合重複且部分整除
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 41, in test_mixed_with_duplicates
    result = clean_data([6, 3, 6, 9, 3], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_negative_numbers (__main__.TestCleanData.test_negative_numbers)
負數也能被整除
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 31, in test_negative_numbers
    result = clean_data([-6, -3, 2, 3], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_no_duplicates_no_match (__main__.TestCleanData.test_no_duplicates_no_match)
無重複但全不整除
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 36, in test_no_duplicates_no_match
    result = clean_data([1, 2, 4, 5], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_none_left (__main__.TestCleanData.test_none_left)
全部被篩掉 -> []
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 16, in test_none_left
    result = clean_data([4, 5, 7], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_preserve_original_order_after_dedupe (__main__.TestCleanData.test_preserve_original_order_after_dedupe)
去重保留第一次出現順序
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 46, in test_preserve_original_order_after_dedupe
    result = clean_data([9, 3, 9, 6, 3], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: test_single_element_divisible (__main__.TestCleanData.test_single_element_divisible)
單一元素且整除
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\test_A01.py", line 26, in test_single_element_divisible
    result = clean_data([6], D=3)
  File "C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041\A01.py", line 2, in clean_data
    raise NotImplementedError
NotImplementedError

----------------------------------------------------------------------
Ran 10 tests in 0.007s

FAILED (errors=10)

給我實作 code 轉綠燈。
我現在　看起來　程式沒有照老師輸出　ＷＨＡＴ　ＰＲＯＢＬＥＭ　ＨＥＲＥ？
我該怎麼　執行我所設計的　程式？
OK
PS C:\Users\User\Downloads\20260622clip> cd weeks/week-18/solutions/1112405041
cd : 找不到 'C:\Users\User\Downloads\20260622clip\weeks\week-18\solutions\1112405041' 路徑，因為它不存在。
位於 線路:1 字元:1
+ cd weeks/week-18/solutions/1112405041
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\User\D...ions\1112405041:String) [Set-Location], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand
 
PS C:\Users\User\Downloads\20260622clip>

你看原始題目 我的 設計 符合題目? 不懂 這邊有 第一題 資料清理 (Data Cleaning) [ A 區 · 保底 ] [ 30 分 ]

步驟①「拿保底」：一份整數資料常有重複與雜訊，請把它清乾淨。本題為學期初已練過的序列 / 字典題型。

相關教材 (可參考)：weeks/week-02/HOMEWORK.md (序列清理)、week-02/bloom-examples/R10-dedupe.py (去重保存)、R09-dict-sets.py。
! 用 AI 前先回答首頁五項檢查表 (簽名 / 邊界 / 例外 / edge case / 驗收)，填滿才開始協作。

～ 一、題目敘述
對每一組整數數列，依序完成三步：①去除重複 (保留第一次出現的順序) → ②只保留能被 D 整除的數 (D 依學號個位，見參數頁) → ③由小到大排序。

～ 二、輸入說明
輸入包含多組測資。每組第一行一個整數 n (1 ≤ n ≤ 10⁵)，表示數列長度；第二行有 n 個以空白分隔的整數 (-10⁹ ≤ a_i ≤ 10⁹)。
當某組的 n = 0 時代表輸入結束，該組不需處理。

～ 三、輸出說明
對每組測資輸出一行：處理後的數列，數字間以單一空白分隔；若沒有任何數字符合，該行輸出 NONE。

～ 四、範例 (Sample, 假設 D = 2)
Sample Input

8
4 7 4 2 9 2 6 7
3
1 3 5
0
Sample Output

2 4 6
NONE
第 1 組：去重保序 → 4 7 2 9 6；能被 2 整除 → 4 2 6；升冪 → 2 4 6。第 2 組無偶數 → NONE。

∠ 先填你的參數，再算「同一組 Sample Input」的預期輸出
我的整除數 D = 3 (個位 u → u%4+2 )
用你的 D 重算上面 Sample Input 的輸出 (兩組)：
第 1 組：______________________
第 2 組：______________________

驗收：PR + TA 隱藏測資 (配分見首頁檢查表)。


所以 我想單跑 A01 測試
所以 我想單跑 A01 測試 (就是我們 寫的 A01.PY
8
4 7 4 2 9 2 6 7
3
1 3 5
0	問答 老師的 CASE D=2 OUTPUT= 246 NONE (我是否沒有還原老師 要求?

PS C:\Users\User\Downloads\20260622clip\2026-python\weeks\week-18\solutions\1112405041> cd C:\Users\User\Downloads\20260622clip\2026-python
PS C:\Users\User\Downloads\20260622clip\2026-python> python weeks\week-18\solutions\1112405041\A01.py
8
4 7 4 2 9 2 6 7                                 
6 9
3
1 3 5
3
0
PS C:\Users\User\Downloads\20260622clip\2026-python>  (這是真實 輸出結果 3 輸出 早於我輸入(壞掉喔?
PS C:\Users\User\Downloads\20260622clip\2026-python> cd C:\Users\User\Downloads\20260622clip\2026-python
PS C:\Users\User\Downloads\20260622clip\2026-python> python weeks\week-18\solutions\1112405041\A01.py
8
47429267
NONE (喔 抓到錯誤了?

好了 那根據 WEEK 15 16 17 (我該做甚麼 文件? 範本也在那裡 幫我抓吧

所以根據這題 的 要求 從 好了 那根據 WEEK 15 16 17 (我該做甚麼 文件? 範本也在那裡 幫我抓吧  真的 只要繳交這些?

我改了什麼 你能舉例 讓我參考?

# AI 給了什麼

> AI 回應重點：

1. 給了 `test_A01.py`，包含 10 個測試案例（基本、空結果、全重複、單一元素、負數、混合重複、去重順序、主程式多組輸出等）
2. 給了 `A01.py` 的 stub 框架（`NotImplementedError` + `main()` 讀取 stdin）
3.幫我根據 ✅簽名 ✅邊界 ✅例外 ✅Edge ✅驗收 逐一測試 教我使用 powershell commit 繳交pr 等等 (是我要求他對格式 輸出正確的pr)
4.給了 我很多 根據題目要求 設計 的 程式 討論我該怎麼 呈現 跟我討論 我該怎麼 設計 教學我懂了 才開始 實作 與他討論跟回答

## 我改了什麼

> **（這欄你自己填，不能空白！）**
> AI 給的 10 個測試案例涵蓋了基本、空結果、負數等 edge case，我確認符合 D=3 的預期輸出後直接採用，沒有修改 
我進行了 手動測試 8
47429267
NONE 
發現該程式 無法針對 黏在一起的數字處理 符合題目要求  但這是我的 edge case 手動額外測試





> 請寫你實際做了什麼判斷或修改：

跟AI 討論為甚麼 

我知道了 

這不是程式錯誤，是輸入格式問題。

你第二行打的是：

47429267
全部黏在一起，沒有空白。程式用 .split() 拆成一個數字 [47429267]，去重後還是 [47429267]，%3 != 0 → NONE。

正確要打：

4 7 4 2 9 2 6 7
每個數字用空白隔開。程式是對的

根據溝通得知OK



## AI 反問我什麼 / 我怎麼回答

> AI 問的規格問題與我的決定：

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 函式簽名叫什麼？參數與回傳？ | `clean_data(nums: list[int], D: int) -> list[int]` |
| D 值怎麼算？ | 學號個位數 1 → 1%4+2 = 3 |
| edge case 要測哪些？ | 全部被篩掉、全部重複、負數整除、單一元素 |
| 空結果輸出什麼？ | 回傳 []，主程式印 NONE |
 (這樣OK 了? 第一個 太長了











 
 
 
 
 
 重點為 「第一題資料清理，輸入多組測資，每組 n + n 個整數，n=0 結束。三步驟：去重保序 → 整除 D 篩選 → 升冪排序。請幫我用 unittest 寫測試，至少包含基本案例、全部被篩掉、全部重複、負數整除等 edge case。」

## AI 給了什麼

> AI 回應重點：

1. 給了 `test_A01.py`，包含 10 個測試案例（基本、空結果、全重複、單一元素、負數、混合重複、去重順序、主程式多組輸出等）
2. 給了 `A01.py` 的 stub 框架（`NotImplementedError` + `main()` 讀取 stdin）
3.幫我根據 ✅簽名 ✅邊界 ✅例外 ✅Edge ✅驗收 逐一測試 教我使用 powershell commit 繳交pr 等等 (是我要求他對格式 輸出正確的pr)
4.給了 我很多 根據題目要求 設計 的 程式 討論我該怎麼 呈現 跟我討論 我該怎麼 設計 教學我懂了 才開始 實作 與他討論跟回答 

## 我改了什麼

> **（這欄你自己填，不能空白！）**
> AI 給的 10 個測試案例涵蓋了基本、空結果、負數等 edge case，我確認符合 D=3 的預期輸出後直接採用，沒有修改 
我進行了 手動測試 8
47429267
NONE 
發現該程式 無法針對 黏在一起的數字處理 符合題目要求  但這是我的 edge case 手動額外測試





> 請寫你實際做了什麼判斷或修改：

跟AI 討論為甚麼 

我知道了 

這不是程式錯誤，是輸入格式問題。

你第二行打的是：

47429267
全部黏在一起，沒有空白。程式用 .split() 拆成一個數字 [47429267]，去重後還是 [47429267]，%3 != 0 → NONE。

正確要打：

4 7 4 2 9 2 6 7
每個數字用空白隔開。程式是對的

根據溝通得知OK



## AI 反問我什麼 / 我怎麼回答

> AI 問的規格問題與我的決定：

| AI 問了什麼 | 我怎麼回答 |
|---|---|
| 函式簽名叫什麼？參數與回傳？ | `clean_data(nums: list[int], D: int) -> list[int]` |
| D 值怎麼算？ | 學號個位數 1 → 1%4+2 = 3 |
| edge case 要測哪些？ | 全部被篩掉、全部重複、負數整除、單一元素 |
| 空結果輸出什麼？ | 回傳 []，主程式印 NONE |
