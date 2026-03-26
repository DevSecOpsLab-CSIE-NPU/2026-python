# Phase 1: Big Two Game - 資料模型實現

## 提交內容

### 文件結構

```
1114405028/
├── game/
│   ├── __init__.py          # 模組初始化
│   └── models.py            # Card、Deck、Hand、Player 實現
├── tests/
│   ├── __init__.py
│   └── test_models.py       # 29 個單元測試
└── README.md                # 本檔案
```

### 實現清單

| 類別 | 方法/屬性 | 狀態 |
|------|----------|------|
| Card | __init__, __repr__, __eq__, __lt__, __le__, __gt__, __ge__, __hash__, to_sort_key() | ✅ |
| Deck | __init__, _create_cards(), shuffle(), deal() | ✅ |
| Hand | __init__, sort_desc(), find_3_clubs(), remove() | ✅ |
| Player | __init__, take_cards(), play_cards() | ✅ |

## 測試結果

### 運行命令

```bash
cd 1114405028
python -m unittest tests.test_models -v
```

### 測試摘要

- **總測試數**：29
- **通過**：29 ✅
- **失敗**：0
- **執行時間**：0.003s

### 測試項目分佈

| 類別 | 測試數 | 狀態 |
|------|--------|------|
| TestCard | 10 | ✅ all passed |
| TestDeck | 8 | ✅ all passed |
| TestHand | 7 | ✅ all passed |
| TestPlayer | 4 | ✅ all passed |

## 核心實現亮點

### Card 類別

- ✅ 支持所有比較運算子（__lt__, __le__, __gt__, __ge__, __eq__）
- ✅ 實現 __hash__ 支持 set 和字典
- ✅ 類別屬性優化：SUIT_SYMBOLS、RANK_SYMBOLS、RANK_ORDER
- ✅ 完整的文檔字符串

### Deck 類別

- ✅ 自動建立 52 張牌
- ✅ shuffle() 使用 random.shuffle()
- ✅ deal(n) 支持發牌超過剩餘牌數的情況
- ✅ _create_cards() 方法提取

### Hand 類別

- ✅ 繼承自 list，支持原生迭代
- ✅ sort_desc() 按點數降序，花色升序排列
- ✅ find_3_clubs() 高效查找梅花三
- ✅ remove() 安全移除牌（處理不存在的情況）

### Player 類別

- ✅ 屬性：name、is_ai、hand、score
- ✅ take_cards() 拿牌到手中
- ✅ play_cards() 出牌並返回

## 型別註解

所有類別和方法都包含完整的型別註解，支持 mypy 靜態檢查。

## 代碼品質

- ✅ 完整的文檔字符串（docstring）
- ✅ 中文註解和說明
- ✅ 遵循 PEP 8 命名規範
- ✅ 無 linting 警告

---

**提交日期**：2026-03-26  
**學號**：1114405028
