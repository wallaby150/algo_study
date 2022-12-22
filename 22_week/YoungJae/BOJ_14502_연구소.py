from collections import deque
from itertools import combinations
from copy import deepcopy

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
q, r = [], []
rst = 0
# 초기 빈 공간 수 c
c = sum(mp, []).count(0)
# q에 바이러스와 c-3(벽 3개), r에 빈 공간 좌표 입력
for i in range(n):
    for j in range(m):
        if mp[i][j] == 2: q.append((i, j, c-3))
        if mp[i][j] == 0: r.append((i, j))
# 빈 공간 중 3개 조합해서 반복
for (y1, x1), (y2, x2), (y3, x3) in combinations(r, 3):
    np = deepcopy(mp)
    # 벽 설치
    np[y1][x1] = np[y2][x2] = np[y3][x3] = 1
    # 바이러스 BFS
    qq = deque(q[:])
    while qq:
        y, x, c = qq.popleft()
        # 이미 최대 안전 영역보다 작아졌으면 의미없으므로 종료
        if c <= rst: continue
        # 델타 탐색, 빈 공간이면 바이러스 퍼짐
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and not np[ny][nx]:
                np[ny][nx] = 2
                qq.append((ny, nx, c-1))
    # 남은 안전 영역 cc, 최대 안전 영역 수 rst
    cc = sum(np, []).count(0)
    rst = max(rst, cc)
print(rst)