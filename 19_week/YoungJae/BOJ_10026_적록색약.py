from collections import deque

# 델타탐색
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
mp = [list(input()) for _ in range(n)]
vs = [[0]*n for _ in range(n)]
# 적록색약이 아닌 경우
cnt1 = 0
# 모든 맵 한 번씩 탐사
for i in range(n):
    for j in range(n):
        # 확인된 구역이 아닌 경우 queue에 추가
        if vs[i][j] == 0:
            q = deque([(i, j, mp[i][j])])
            # 파랑만 1로 나머진 2로 vs에 저장, 이후 적록색맹일 때는 vs로 확인할 예정
            vs[i][j] = 2 if mp[i][j] == 'B' else 1
            # 구역 개수 + 1
            cnt1 += 1
            # BFS
            while q:
                y, x, c = q.popleft()
                for a in range(4):
                    ny, nx = y+dy[a], x+dx[a]
                    # 방문한 적 없고 같은 색일 때 확장
                    if 0 <= ny < n and 0 <= nx < n and vs[ny][nx] == 0 and mp[ny][nx] == c:
                        q.append((ny, nx, mp[ny][nx]))
                        vs[ny][nx] = 2 if mp[ny][nx] == 'B' else 1
# 적록색맹인 경우
cnt2 = 0
for i in range(n):
    for j in range(n):
        if vs[i][j] != 0:
            q = deque([(i, j, vs[i][j])])
            cnt2 += 1
            # BFS
            while q:
                y, x, c = q.popleft()
                for a in range(4):
                    ny, nx = y+dy[a], x+dx[a]
                    if 0 <= ny < n and 0 <= nx < n and vs[ny][nx] == c:
                        q.append((ny, nx, vs[ny][nx]))
                        vs[ny][nx] = 0
print(f'{cnt1} {cnt2}')