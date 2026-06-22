# Week 17 Binary Search Performance Evaluation (6/18 Search Lab)

## 本週目標

- 實作線性搜尋與二分搜尋
- 使用 timeit 量測搜尋效能
- 分析不同搜尋演算法在不同數據規模下的表現
- 畫雷達圖呈現多維權衡
- 輸出最終評估報告

## 執行方式

### Python 版本

- Python 3.9+

### 執行指令

```bash
# 建立虛擬環境 (可選)
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 安裝依賴
pip install matplotlib

# 運行測量
python benchmark.py

# 生成雷達圖
python plot.py
```

### 測試執行

```bash
# 執行所有單元測試
python -m unittest test_timing test_search test_plot test_security -v
```

## 依賴套件

- **matplotlib** - 雷達圖繪圖
- **Python 標準庫** - 其他功能

## 補充說明

### 專題概述

本專題為期末考 **B 區候選池** 搜尋效能實驗室。

### 實作內容

1. **基礎搜尋實現**
   - `linear_search(data, target)` - 線性搜尋，返回索引或 -1
   - `binary_search(data, target)` - 二分搜尋，返回索引或 -1
   - `set_search(data, target)` - Hash 搜尋，返回布林值

2. **效能量測**
   - 使用 timeit 裝飾器比較搜尋效能
   - 測試不同數據規模 (10000, 50000, 100000)
   - 比較基準 (內建 `in`, `bisect`) 與自實現版本

3. **性能評估**
   - 輸出每種搜尋算法的執行时间
   - 判斷哪种方法更快
   - 进行多维权衡分析

4. **雷达图可视化**
   - 绘制雷达图呈现三种搜索算法的性能比较
   - 分析不同维度上的优劣势
   - 生成 `assets/radar.png`

### 技术实现

1. **timeit 装饰器**
   - 记录执行时间
   - 支持 repeat 参数
   - 提供 records 和 last_elapsed 属性

2. **搜索算法**
   - 线性搜索：O(n) 最坏情况
   - 二分搜索：O(log n) 最坏情况，需要排序
   - Hash 搜索：O(1) 平均情况，需要额外空间

3. **性能评估**
   - 比较不同数据规模下的表现
   - 分析小规模 vs 大规模效能
   - 评估实现复杂度

### 输出结果

1. **benchmark.py 输出**
   ```
   Data size: 10000
   Linear search (baseline):   0.001234 s
   Binary search (baseline):   0.000567 s
   Linear search (Python):     0.002345 s
   Binary search (Python):     0.001123 s
   Faster method: binary
   ```

2. **雷达图**
   - 呈现五个维度：小规模速度、大规模速度、是否需要排序、实现复杂度、最坏情况比较次数
   - 展示各搜索算法在这些维度上的表现
   - 生成 PNG 文件：`assets/radar.png`

### 验证

```bash
# 所有单元测试应通过
python -m unittest test_timing test_search test_plot test_security -v
# 输出:
OK
```

### 如何通过测试

1. 确保所有单元测试通过
2. 运行 benchmark.py 生成 results.json
3. 运行 plot.py 生成雷达图
4. 确认 assets/radar.png 已生成

### 雷达图解读

雷达图呈现五个维度：

1. **Small n Speed**: 小规模数组时的速度比较
2. **Large n Speed**: 大规模数组时的速度比较
3. **Setup Cost**: 是否需要预先排序
4. **Implementation**: 实现复杂度
5. **Worst Case**: 最坏情况比较次数

每个搜索算法在这些维度上的表现不同，没有绝对的赢家，只有针对特定场景的最佳选择。

### 安全要求

- **OpenSSF 安全编码指南**：
  - 使用具体的例外处理 (FileNotFoundError, ValueError 等)
  - 使用 with 语句安全开启文件
  - 避免使用隐藏的内置名称
  - 使用 json 而非 pickle 读取文件

- 所有安全规则的测试都已纳入 test_security.py

### 时间复杂度与空间复杂度

| 算法 | 时间复杂度 | 空间复杂度 |
|---------|------------|------------|
| 线性搜索 | O(n) | O(1) |
| 二分搜索 | O(log n) | O(1) |
| Hash 搜索 | O(1) 平均 | O(n) |

### 数据集

- **数据规模**：10000, 50000, 100000
- **数据范围**：0-1000000
- **目标 K**：121 (100 + 学号末两码)

### 未来改进

1. **并行处理**：并行比较多种搜索算法
2. **记忆化**：缓存排序结果
3. **自适应搜索**：动态选择最佳搜索算法
4. **可视化仪表盘**：交互式性能比较工具

---

**谢谢！** 希望这个搜索性能评估实验室能帮助您理解不同搜索算法的性能特点。祝您好运！
