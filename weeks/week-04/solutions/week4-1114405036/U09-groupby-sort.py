# U9. groupby 為何一定要先 sort（範例 1.15）
# 原理：itertools.groupby 的實作邏輯是「掃描」序列，只要下一個元素與目前不同就開新組。
# 若沒排序，相同的 key 可能分散在不同段落，導致分組失敗。

from itertools import groupby
from operator import itemgetter

rows = [{'date': '07/02'}, {'date': '07/01'}, {'date': '07/02'}]
# 若不 sort，結果會產生三個分組（07/02, 07/01, 07/02）
# sort 後，兩個 07/02 會連在一起，合併成同一個分組。