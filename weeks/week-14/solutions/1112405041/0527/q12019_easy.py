# [AI Easy] Defensive logic against magic-mods
import datetime, sys
def solve():
 d=sys.stdin.read().split(); if not d: return
 t=int(d[0]); p=1; days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
 for _ in range(t):
  m,dy=int(d[p]),int(d[p+1]); p+=2; dt=datetime.date(2012, m, dy); print(days[dt.weekday()])
if __name__=='__main__': solve()
