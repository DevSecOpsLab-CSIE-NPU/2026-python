import sys
import math
import bisect

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)
        except StopIteration:
            break
        
        segments = []
        events = []
        
        for i in range(n):
            sx = int(next(iterator))
            sy = int(next(iterator))
            ex = int(next(iterator))
            ey = int(next(iterator))
            
            # 計算兩端點的極角
            ang1 = math.atan2(sy, sx)
            ang2 = math.atan2(ey, ex)
            
            # 確保 ang1 < ang2
            if ang1 > ang2:
                ang1, ang2 = ang2, ang1
                sx, sy, ex, ey = ex, ey, sx, sy
            
            # 處理跨越 -pi / pi 邊界的情況
            # 如果角度差大於 pi，說明它跨越了極軸邊界，將其拆分成兩段
            if ang2 - ang1 > math.pi:
                # 第一段: [-pi, ang1]
                segments.append((sx, sy, ex, ey, i))
                seg_idx = len(segments) - 1
                events.append(( -math.pi, 1, seg_idx )) # 1 代表進入
                events.append(( ang1, -1, seg_idx ))    # -1 代表離開
                
                # 第二段: [ang2, pi]
                events.append(( ang2, 1, seg_idx ))
                events.append(( math.pi, -1, seg_idx ))
            else:
                segments.append((sx, sy, ex, ey, i))
                seg_idx = len(segments) - 1
                events.append((ang1, 1, seg_idx))
                events.append((ang2, -1, seg_idx))
        
        # 按照極角排序事件。若極角相同，離開事件(-1)優先於進入事件(1)以防邊界漏判
        events.sort(key=lambda x: (x[0], x[1]))
        
        # 用於記錄每個鏡子是否可見
        visible = [0] * n
        
        # 當前被掃描線穿過的鏡子集合（儲存 seg_idx）
        active_segments = []
        
        # 輔助函式：計算在特定極角下，射線與指定線段的交點到原點的距離平方
        # 這裡用距離平方可以避免開根號以提升效能與精確度
        def get_dist_sq(seg_idx, angle):
            sx, sy, ex, ey, _ = segments[seg_idx]
            # 射線方向向量
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            
            # 線段參數式：P(t) = (sx + t*(ex-sx), sy + t*(ey-sy)), 0 <= t <= 1
            # 射線與線段交點滿足： P(t) 叉積 射線方向 = 0
            # (sx + t*dx)*sin_a - (sy + t*dy)*cos_a = 0
            dx = ex - sx
            dy = ey - sy
            
            denom = dy * cos_a - dx * sin_a
            if abs(denom) < 1e-9:
                # 平行情況，回傳兩端點較近者的距離平方
                return min(sx*sx + sy*sy, ex*ex + ey*ey)
                
            num = sy * cos_a - sx * sin_a
            t = num / denom
            t = max(0.0, min(1.0, t)) # 確保交點在線段內
            
            ix = sx + t * dx
            iy = sy + t * dy
            return ix*ix + iy*iy

        # 為了在 active_segments 中保持依距離排序，定義比較類別
        class SweepNode:
            def __init__(self, idx):
                self.idx = idx
            def __lt__(self, other):
                # 依據當前掃描線角度比較兩鏡子的距離
                return get_dist_sq(self.idx, current_angle) < get_dist_sq(other.idx, current_angle)

        current_angle = -math.pi
        active_nodes = [] # 儲存 SweepNode
        
        # 開始極角掃描
        for ang, event_type, seg_idx in events:
            current_angle = ang
            
            if event_type == 1: # 進入事件
                node = SweepNode(seg_idx)
                bisect.insort(active_nodes, node)
            else: # 離開事件
                # 尋找並移除該鏡子
                # 由於 Python 的 bisect 在自定義物件動態改變順序時可能不精準，
                # 且 n 雖然大但 active 集合通常很小，這裡直接線性尋找移除
                for k, node in enumerate(active_nodes):
                    if node.idx == seg_idx:
                        active_nodes.pop(k)
                        break
            
            # 每次事件發生時，最前面的鏡子就是可見的
            if active_nodes:
                nearest_seg_idx = active_nodes[0].idx
                orig_idx = segments[nearest_seg_idx][4]
                visible[orig_idx] = 1

        # 輸出結果，鏡子之間用空格相連
        print(" ".join(map(str, visible)))

if __name__ == '__main__':
    solve()