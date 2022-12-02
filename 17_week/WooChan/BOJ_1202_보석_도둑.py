# https://www.acmicpc.net/problem/1202
import sys
sys.stdin = open('input.txt')

## Solve 1
## 암산으로 적고서 '쩔었다' 생각했는데
## 시간초과
## 풀이에 없어도 되는 군더더기도 있다.
# N, K = map(int, sys.stdin.readline().split())
#
# jewel = [0] * N
# bag = [0] * K
# get_jewel = [0] * N
# get_bag = [0] * K
# count = 0
#
# for i in range(N):
#     M, V = map(int, sys.stdin.readline().split())
#     jewel[i] = (M, V, i)
#
# for i in range(K):
#     C = int(sys.stdin.readline())
#     bag[i] = C
#
# sorted(jewel, key=lambda jewel : jewel[0], reverse=True)
# sorted(bag)
#
# for i in range(N):
#     for j in range(K):
#         if get_bag[j] == 0 and jewel[i][0] <= bag[j]:
#             get_bag[j] = (jewel[i][1], j, jewel[i][2])
#             get_jewel[jewel[i][2]] = 1
#             count += 1
#             break
#
#     if count == K:
#         break
#
# sorted(jewel, key=lambda jewel : jewel[1], reverse=True)
# sorted(get_bag, key=lambda get_bag : get_bag[0])
#
# for i in range(N):
#     if get_jewel[jewel[i][2]] == 0:
#         for j in range(K):
#             if jewel[i][1] > get_bag[j][0] and bag[get_bag[j][1]] >= jewel[i][0]:
#                 get_jewel[jewel[i][2]] = 1
#                 get_jewel[get_bag[j][2]] = 0
#                 get_bag[j] = (jewel[i][1], get_bag[j][1], jewel[i][2])
#                 break
#
# answer = 0
# for i in get_bag:
#     answer += i[0]
#
# print(answer)


## Solve 2
## 위의 풀이에서 군더더기를 빼고 더 간단하게 풀이
## 시간초과
# N, K = map(int, sys.stdin.readline().split())
#
# jewel = [0] * N
# bag = [0] * K
# bag_full = [0] * K
# get = [0] * K
#
# for i in range(N):
#     M, V = map(int, sys.stdin.readline().split())
#     jewel[i] = (M, V)
#
# for i in range(K):
#     C = int(sys.stdin.readline())
#     bag[i] = C
#
# sorted(jewel, key=lambda jewel : jewel[1], reverse=True)
# sorted(bag)
#
# for i in range(N):
#     for j in range(K):
#         if bag_full[j] == 0 and jewel[i][0] < bag[j]:
#             get[j] = jewel[i][1]
#             bag_full[j] = 1
#             break
#
# print(sum(get))


## Solve 3
## deque를 이용, sorted() 대신 버블정렬
## 의미 없음
## 시간초과
# from collections import deque
# N, K = map(int, sys.stdin.readline().split())
#
# jewels = deque()
# bag = [0] * K
# bag_full = [0] * K
# get = [0] * K
#
# for i in range(N):
#     M, V = map(int, sys.stdin.readline().split())
#     jewels.append((M, V))
#
# for i in range(K):
#     C = int(sys.stdin.readline())
#     bag[i] = C
#
# for i in range(len(jewels)):
#     for j in range(len(jewels)-1, i, -1):
#         if jewels[j][1] < jewels[j-1][1]:
#             jewels[j], jewels[j-1] = jewels[j-1], jewels[j]
#
# sorted(bag)
#
# while jewels:
#     jewel = jewels.pop()
#     for j in range(K):
#         if bag_full[j] == 0 and jewel[0] < bag[j]:
#             get[j] = jewel[1]
#             bag_full[j] = 1
#             break
#
# print(sum(get))


## Solve 4
## heapq 써야한다길래 공부 후 사용
import heapq
N, K = map(int, sys.stdin.readline().split())

jewels = []     # 보석
bags = []       # 가방
get = []        # 현재 가방에 넣을 수 있는 보석들
answer = 0

# 보석을 무게 순 정렬
for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewels, (M, V))

# 가방을 무게 순 정렬
for i in range(K):
    C = int(sys.stdin.readline())
    heapq.heappush(bags, C)


while bags:
    bag = heapq.heappop(bags)       # 용량이 작은 가방부터 확인
    while jewels and jewels[0][0] <= bag:       # 아직 확인 안한 보석이 있고 그 중 가장 가벼운 보석이 현재 가방에 들어가면
        heapq.heappush(get, -heapq.heappop(jewels)[1])      # 그 보석을 jewel에서 빼고 get에 넣는다
    if get:     # 현재 가방에 넣을 수 있는 보석이 있으면
        answer += -heapq.heappop(get)       # 가장 가치가 높은 보석을 넣어준다

print(answer)