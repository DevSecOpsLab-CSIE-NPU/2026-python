# Week 18 新版本提交

這是一份與原始版本分離的新資料夾，內容為英文字母位移加密程式。

## 執行方式

```bash
python main.py < input.txt
python -m unittest test_main -v
```

## 說明

- `SHIFT = 2`
- 逐行讀到 EOF
- 大小寫分開循環
- 非字母原樣保留