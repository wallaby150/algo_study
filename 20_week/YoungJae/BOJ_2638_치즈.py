import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
# 보석 저장
# 무게 순으로 heappush
jew = []
for _ in range(n): heapq.heappush(jew, list(map(int, input().split())))
# 가방 저장 후 무게 오름차순 정렬
bag = []
for _ in range(k): bag.append(int(input()))
bag.sort()
# 결과
rst = 0
# 가방에 담을 수 있는 보석의 가치 저장용 tmp
tmp = []
# 작은 가방부터 채우기
for b in bag:
    # 넣을 수 있는 보석들을 tmp에 가격순으로 넣기
    while jew and b >= jew[0][0]: heapq.heappush(tmp, -heapq.heappop(jew)[1])
    # 그 중 가장 값어치 있는 보석을 넣음
    if tmp: rst -= heapq.heappop(tmp)
    # 보석이 더 없으면 종료
    elif not jew: break
print(rst)