from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# 도로 기록
rd = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, p = map(int,input().split())
    rd[s].append((e, p))
# 출발지점/도착지점 확인
s, e = map(int,input().split())
# 비용 저장용 cs, 최초값은 최댓값보다 크게
cs = [1e9]*(n+1)
# 출발지는 비용 0
cs[s] = 0
# 이동경로 저장용 rst, 출발지는 자기 지역만
rst = [[] for _ in range(n+1)]
rst[s] = [s]
# heapq 생성
q = [(0, s)]
# dijkstra
while q:
    c, v = heappop(q)
    if c > cs[v]: continue
    # 더 적은 비용이면 갱신하고 rst에 경로 저장 후 heappush
    for l, d in rd[v]:
        if cs[l] > c + d: cs[l] = c + d; rst[l] = rst[v]+[l]; heappush(q, (c + d, l))
print(cs[e])
print(len(rst[e]))
print(*rst[e])