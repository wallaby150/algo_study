import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# BOJ 1976 여행 가자

N = int(input())    # N : 도시의 수
M = int(input())    # M : 여행 계획에 속한 도시 수
path = [list(map(int,input().split())) for _ in range(N)]  # 연결 여부
plan = list(map(int,input().split())) # 여행 계획. 1번 도시부터~

for s in range(len(plan)-1):
    start, goal = plan[s] - 1, plan[s + 1] - 1  # 인덱스로 사용하려고 -1
    # BFS. start에서 bfs 돌려서 goal을 만나면 for문 돌아서 다음 목적지 bfs
    # 만약 start에서 goal에 도달하지 못하면 NO 출력
    q = deque([start])
    visit = [0 for _ in range(N)]
    canGo = False
    while q:
        next = q.popleft()
        visit[next] = 1
        if next == goal:
            canGo = True
            break
        for i in range(N):
            # 방문하지 않았고, 갈 수 있는 곳이면 queue에 추가
            if path[next][i] == 1 and visit[i] == 0:
                q.append(i)
    if not canGo:
        print('NO')
        break
    if canGo and s == len(plan)-2:
        print('YES')
        break
