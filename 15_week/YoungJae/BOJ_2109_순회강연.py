# 1차 방법

import heapq

n = int(input())
q = []
t = 0
# 일자, 가격 heapq에 추가
# 오름차순 정렬이 default이므로 -p로 입력
# t에 최대 일자 갱신
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(q, (-p, d))
    t = max(t, d)
# 결과 r 생성
r = [0]*(t+1)
# heappop으로 뽑으면서 가장 가까운 일자에 추가
while q:
    p, d = heapq.heappop(q)
    while d > 0:
        if not r[d]: r[d] = -p; break
        d -= 1
print(sum(r))

# 2차

from heapq import *

n = int(input())
# 시간 저장할 리스트 생성
t = [[] for i in range(10001)]
# 각 시간에 append로 추가
for _ in range(n):
    p, d = map(int, input().split())
    t[d].append(p)
q = []
rst = 0
# 역순으로 하며 일이 있으면 heapq에 추가
# 이후 할 수 있는 일이 있으면 추가하는걸 매일 체크
for i in range(10000, 0, -1):
    for x in t[i]: heappush(q, -x)
    if q: rst += -heappop(q)
print(rst)