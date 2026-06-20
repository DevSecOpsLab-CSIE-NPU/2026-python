# Robot Lost

有 6x6 地圖，用 L/R/F 控制機器人，走出邊界會 LOST。第二台機器人可以繼承 scent 避免掉下去。

## 怎麼跑

```
pip install pygame
python robot_game.py
```

按 N 加機器人、L/R/F 轉彎前進、C 清除 scent。

## 怎麼測

```
python -m unittest discover -v
```

27 tests 全過。
