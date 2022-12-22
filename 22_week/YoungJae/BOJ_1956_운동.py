# 1. 플로이드-워셜(pypy3)

v, e = map(int, input().split())
# 그래프 행렬 dr
dr = [[1e8]*v for _ in range(v)]
# 도로 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    dr[a-1][b-1] = c
# 플로이드-워셜
for k in range(v):
    for i in range(v):
        for j in range(v): dr[i][j] = min(dr[i][j], dr[i][k] + dr[k][j])
# 대각성분만 가져오면 자기자신으로 돌아오는 최소거리가 됨
x = min([dr[i][i] for i in range(v)])
print(x) if x < 1e8 else print(-1)

#############################################################
# 2. dijkstra 응용(python 3)

from heapq import *
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
# 값 저장용 dp
dp = [[1e8]*(v+1) for _ in range(v+1)]
# 그래프 딕셔너리 rd
rd = {i: [] for i in range(v+1)}
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    # dp와 rd, heapq에 추가
    dp[a][b] = c
    rd[a].append((c, b))
    heappush(q, (c, a, b))
# dijkstra 응용
# heapq이므로 최소값부터 처리됨
while q:
    c, a, b = heappop(q)
    # 출발지 도착지가 같은 경우 최소 사이클이 나왔으므로 출력하고 종료
    if a == b: print(c); break
    # 최소값 아니면 패스
    if c > dp[a-1][b]: continue
    # a > b > r이 a > r보다 짧으면 갱신
    for k, r in rd[b]:
        if c + k < dp[a][r]:
            dp[a][r] = c + k; heappush(q, (c+k, a, r))
# break가 안나왔으면 사이클이 없는 것이므로 -1 출력
else: print(-1)