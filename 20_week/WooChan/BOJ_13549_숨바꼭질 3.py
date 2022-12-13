# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
# N, K = map(int, input().split())

# 동생이 뒤에 있을 때
if N >= K:
    print(N - K)

# 동생이 앞에 있을 때
else:
    time = [-1] * 100001

    stack = deque()
    stack.append(N)
    time[N] = 0

    while stack:
        locate = stack.popleft()

        # 동생 발견
        if locate == K:
            break

        # 순간이동
        next_locate = locate * 2
        if 0 < next_locate <= 100000 and time[next_locate] == -1:
            time[next_locate] = time[locate]
            stack.appendleft(next_locate)       # 순간이동 먼저

        # 뒤로 한 칸
        next_locate = locate - 1
        if 0 <= next_locate <= 100000 and time[next_locate] == -1:
            time[next_locate] = time[locate] + 1
            stack.append(next_locate)

        # 앞으로 한 칸
        next_locate = locate + 1
        if 0 <= next_locate <= 100000 and time[next_locate] == -1:
            time[next_locate] = time[locate] + 1
            stack.append(next_locate)

    print(time[K])


# time = 0
# if N >= K:
#     time = N - K
#     print(time)
# else:
#     n = 0
#     if N == 0:
#         locate = 1
#         time += 1
#     else:
#         locate = N
#
#     while locate <= K:
#         locate *= 2
#         n += 1
#
#     distance_a = K - (locate//2)
#     time_a = time
#     n_a = n-1
#
#     distance_b = locate - K
#     time_b = time
#     n_b = n
#
#     while distance_a > 0:
#         a_a = 2**n_a
#         if distance_a - a_a >= 0:
#             distance_a -= a_a
#             time_a += 1
#
#         else:
#             n_a -= 1
#
#     while distance_b > 0:
#         a_b = 2**n_b
#         if distance_b - a_b >= 0:
#             distance_b -= a_b
#             time_b += 1
#
#         else:
#             n_b -= 1
#
#     print(min(time_a, time_b))