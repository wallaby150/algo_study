# https://www.acmicpc.net/problem/1956
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

V, E = map(int, input().split())

road = list([0] * V for _ in range(V))

for _ in range(E):
    a, b, c = map(int, input().split())
    road[a-1][b-1] = c

def bfs(start, now, distance):
    global answer

    if distance > answer:
        return

    if now == start and visited[start] == 1:
        if distance < answer:
            answer = distance
        return

    for next in range(V):
        if road[now][next] != 0 and visited[next] == 0:
            visited[next] = 1
            bfs(start, next, distance + road[now][next])
            visited[next] = 0

visited = [0] * V

answer = 10001 * E

for start in range(V):
    bfs(start, start, 0)

if answer == 10001 * E:
    print(-1)
else:
    print(answer)