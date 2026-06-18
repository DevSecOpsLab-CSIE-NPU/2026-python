import sys; from collections import deque
def solve():
 d=sys.stdin.read().split(); if not d: return
 N,M,T=map(int, d[:3]); g=[[0]*M for _ in range(N)]; p=3
 def can():
  q=deque([(r,0) for r in range(N) if g[r][0]==0]); v=set(q)
  while q:
   r,c=q.popleft(); if c==M-1: return True
   for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr,nc=r+dr,c+dc; if 0<=nr<N and 0<=nc<M and g[nr][nc]==0 and (nr,nc) not in v:
     v.add((nr,nc)); q.append((nr,nc))
  return False
 for _ in range(T):
  x,y=int(d[p]),int(d[p+1]); p+=2; g[x][y]=1
  if can(): print('<(_ _)>')
  else: g[x][y]=0; print('>_<')
if __name__=='__main__': solve()
