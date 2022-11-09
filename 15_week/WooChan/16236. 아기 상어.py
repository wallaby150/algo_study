'''
https://www.acmicpc.net/problem/16236

[문제]

N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다.
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

    - 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    - 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
        - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
        - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다.
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다.
물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

'''
import sys
from collections import deque

N = int(sys.stdin.readline())

# 아쿠아리움
aquarium = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상어 위치 찾기
# 위치 찾으면 저장
# 먹이 찾을 때 방해 안되게 0으로 변경
for i in range(N):
    for j in range(N):
        if aquarium[i][j] == 9:
            shark = [i, j]
            aquarium[i][j] = 0
            break

direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]

# BFS
stack = deque()
stack.append(shark)

# 해당 위치까지 가는데 걸리는 시간 기록용 visited
visited = [[-1]*N for _ in range(N)]
visited[shark[0]][shark[1]] = 0

distance = 1000     # 가까운 먹이를 찾기 위한 변수
size = 2        # 상어 크기
T = 0       # 엄마 상어 없이 버틴 시간
eat = 0     # 먹은 물고기
fish = []       # 같은 거리에 있는 먹이 중 먹을 물고기를 고르기 위한 list

while stack:        # 갈 수 있는 곳이 없을 때까지 진행
    [x, y] = stack.popleft()        # 상어 현재 위치

    # distance에는 가장 가까운 물고기까지의 거리를 저장
    # distance에 저장된 거리보다 먼 곳을 찾기 시작하면 그만두고 먹이를 고른다
    if visited[x][y] > distance:        # 먹이 후보들을 다 찾았으면
        # 위에 있는 순서, 같은 높이면 왼쪽에 있는 순서대로 정렬
        fish.sort(key=lambda x:x[1])
        fish.sort(key=lambda x:x[0])

        shark = fish[0]     # 물고기 먹으러 상어 이동
        aquarium[shark[0]][shark[1]] = 0        # 물고기가 먹혀서 빈 자리가 되었습니다...

        eat += 1        # 먹은 물고기 숫자 +1
        if eat == size:     # 충분히 먹었으면
            size += 1       # 성장
            eat = 0     # 소화 끝나서 다시 배고프다

        T += visited[shark[0]][shark[1]]        # 물고기 먹으러 이동하는 데 걸린 시간 추가

        # 먹이 찾기 다시 시작
        stack.clear()
        stack.append(shark)
        fish = []
        visited = [[-1] * N for _ in range(N)]
        visited[shark[0]][shark[1]] = 0
        distance = 1000
        # 현재 상어 위치 갱신
        [x, y] = stack.popleft()

    # 먹이 후보가 있으면
    if 0 < aquarium[x][y] < size:
        if not fish:        # 처음 찾은 먹이 후보면 거리 저장
            distance = visited[x][y]
        fish.append([x, y])     # 먹이 후보로 저장

    # 먹이 찾기 BFS
    for i in range(4):
        next_x = x + direction[i][0]
        next_y = y + direction[i][1]
        if 0 <= next_x < N and 0 <= next_y < N:
            if visited[next_x][next_y] == -1:
                if aquarium[next_x][next_y] <= size:
                    stack.append([next_x, next_y])
                    visited[next_x][next_y] = visited[x][y] + 1

    # 먹이 후보를 찾는 distance의 허점때문에 만든 조건
    # distance보다 먼 곳이 없으면 먹이를 안먹고 끝나버린다.
    if not stack:
        if fish:
            fish.sort(key=lambda x:x[1])
            fish.sort(key=lambda x:x[0])
            shark = fish[0]
            stack.clear()
            stack.append(shark)
            aquarium[shark[0]][shark[1]] = 0
            fish = []

            T += visited[shark[0]][shark[1]]
            visited = [[-1] * N for _ in range(N)]
            visited[shark[0]][shark[1]] = 0
            eat += 1
            if eat == size:
                eat = 0
                size += 1
            distance = 1000

print(T)