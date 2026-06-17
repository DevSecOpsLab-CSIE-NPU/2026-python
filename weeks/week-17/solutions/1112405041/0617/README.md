# 0617 搜尋效能評估

## 量測結果

```
linear 花了: 0.001613 秒
binary 花了: 0.000003 秒
```

## 評估

1. binary_search 比 linear_search 快很多
2. 但 binary 要先排序才能用，排序要花時間
3. 查很多次時，排序一次用 binary 才划算；只查一次的話 linear 可能更快
