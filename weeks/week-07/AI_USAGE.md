# AI 使用說明 (AI_USAGE.md)

## 允許使用 AI 的時機

- 不懂如何寫測試時
- 實現遇到 Python 語法問題時
- ASCII 視覺化時需要靈感時
- 需要重構代碼時

## 禁止使用 AI 的地方

- 完整複製 AI 生成的代碼
- 跳過 TDD 三階段流程
- 使用 `as any` 或 `@ts-ignore` 等方式壓制錯誤

## 推薦作法

1. **先自己寫測試** - 按照 TDD 流程，先寫測試再看失敗
2. **看測試失敗 (RED)** - 確認測試有意義
3. **AI 協助實現 (GREEN)** - 向 AI 請問語法或邏輯問題
4. **自己重構 (REFACTOR)** - 親自重構代碼提升品質
5. **確認所有測試通過** - 保持測試綠燈

## 作業繳交清單

```
week-07/
├── HOMEWORK.md                 ← 說明文件
├── generals.txt                ← 武將資料 (9位)
├── battles.txt                 ← 戰役配置
├── solutions/
│   ├── chibi_battle.py         ← 手寫版核心引擎
│   ├── chibi_battle_easy.py    ← AI 簡化版
│   ├── test_chibi.py           ← 測試檔 (>=12個)
│   └── TEST_LOG.md             ← 測試日誌
└── AI_USAGE.md                 ← 本文件
```

## 學習目標

本作業整合以下技能：

| 項目 | 說明 |
|-----|------|
| **TDD** | Red → Green → Refactor 三階段 |
| **Week 02** | sorted, Counter, defaultdict, namedtuple |
| **Week 07** | 檔案 I/O, EOF 輸入處理 |
| **設計思想** | 資料驅動 + 統計分析 + 視覺化 |
| **測試寫作** | unittest, setUp/tearDown, Arrange-Act-Assert |
