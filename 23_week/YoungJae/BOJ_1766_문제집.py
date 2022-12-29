from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 해당 문제를 풀면 풀 수 있는 문제 목록 pr, 먼저 풀면 좋은 문제 수 ch
pr = [[] for _ in range(n+1)]
ch = [0] * (n + 1)
# pr, ch에 값 저장
for _ in range(m):
    a, b = map(int, input().split())
    pr[a].append(b); ch[b] += 1
# heapq, 결과 저장 리스트 q, rst
q = []
rst = []
# 조건 없이 풀 수 있는 문제들 먼저 q에 저장
for i in range(1, n+1):
    if not ch[i]: q.append(i)
# 우선순위로 BFS
while q:
    x = heappop(q)
    # 풀었으니 rst에 추가
    rst.append(x)
    # ch 1 빼고 0이면 q에 추가
    for y in pr[x]:
        ch[y] -= 1
        if not ch[y]: heappush(q, y)
print(*rst)