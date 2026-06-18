# AI_LOG

## 我問 AI 什麼

> 請依 0617 規格幫我完成 `timeit`、`search`、測試，並在 `README.md` 寫出 linear vs binary 的效能評估。

## AI 給了什麼

> 提供 `timeit` 與搜尋函式實作、對應 `unittest` 測試、效能量測指令與結果整理。

## 我改了什麼

> 一開始把 `binary_search` 設計成每次都檢查是否已排序，造成效能退化；我改成在 docstring 定義「未排序行為未定義」，讓二元搜尋維持應有效率。

## AI 反問我什麼 / 我怎麼回答

> AI 問：`binary_search` 遇到未排序資料要拋錯還是定義為未定義行為？
> 我答：定義為未定義行為，並在 docstring 清楚說明，避免每次呼叫都做 O(n) 檢查。

> AI 問：`timeit` 是否要支援 `@timeit(repeat=...)`？
> 我答：要，並保留 `@timeit` 的預設 `repeat=3` 用法。

> AI 問：`repeat < 1` 的輸入驗證要用什麼方式？
> 我答：用 `raise ValueError`，不要使用 `assert`。
