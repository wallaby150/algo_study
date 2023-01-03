# https://www.acmicpc.net/problem/3096
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

connect = list([] for _ in range(N+1))                          # connect[a][b] : 왼쪽 a마을과 오른쪽 b마을이 연결
for _ in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)


sum_list = [0] * (N+2)                                          # sum_list[i] : 1부터 i-1까지의 합
for i in range(2, N+2):                                         # [0, 0, 1, 1+2, 1+2+3, ...]
    sum_list[i] = sum_list[i-1] + i-1


def num(a, b):                                                  # num(a, b) : 왼쪽 a, b 마을을 선택했을 때, 영화제를 개최할 수 있는 경우의 수
    return sum_list[len(set(connect[a]) & set(connect[b]))]     # sum_list[a, b 마을과 모두 연결된 오른쪽 마을의 수]

answer = 0
for i in range(1, N):                                           # 왼쪽에서 두 개의 마을을 선택했을 때 가능한 경우의 수를 answer에 더해준다.
    for j in range(i+1, N+1):
        answer += num(i, j)

print(answer)