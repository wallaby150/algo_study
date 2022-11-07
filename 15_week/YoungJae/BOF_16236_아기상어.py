from collections import deque

# 델타탐색용, 위를 우선하고 좌측을 우선하므로 상좌우하 순서
dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]

n = int(input())
mp = []
# 크기별 물고기 개수
fs = [0]*7
# 상어 크기 sl, 경험치 exp
sl, exp = 2, 0
# map 추가하면서 상어 위치와 물고기 개수 파악
for i in range(n):
    mp.append(list(map(int,input().split())))
    for j in range(n):
        if mp[i][j] == 9: sk = deque([(i, j, 0)])
        elif mp[i][j] != 0: fs[mp[i][j]] += 1
yy, xx, cc = sk[0]
while 1:
    # 모든 물고기를 잡아먹었으면 종료
    if sum(fs[:sl]) == 0: break
    # 방문여부 확인용 vs
    vs = [[0] * n for _ in range(n)]
    # 현재 상어 위치에 방문표시/상어 제거
    vs[sk[0][0]][sk[0][1]] = 1
    mp[sk[0][0]][sk[0][1]] = 0
    # 먹잇감 리스트 tmp
    tmp = []
    # 최소 이동거리 저장용 st
    st = -1
    # BFS
    while sk:
        y, x, c = sk.popleft()
        # 이미 같은 거리만큼 이동해서 먹잇감 먹은 적이 있으면 종료
        if c == st: break
        # 상어 크기보다 낮은 먹이감이 있으면 st를 c+1로 변경 후 tmp에 추가
        if 0 < mp[y][x] < sl:
            st = c + 1
            tmp.append((y, x, c))
        # 델타탐색
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            # 맵 안이고 방문한 적 없고 상어보다 크지 않은 물고기가 있으면 지나갈 수 있음
            # 방문표시 해주고 sk에 추가
            if 0 <= ny < n and 0 <= nx < n and not vs[ny][nx] and mp[ny][nx] <= sl:
                vs[ny][nx] = 1; sk.append((ny, nx, c+1))
    # tmp에 아무것도 없으면 원상복귀 후 break
    if not tmp: sk = [(yy, xx, cc)]; break
    # tmp y, x 순으로 정렬
    tmp.sort(key = lambda x: (x[0], x[1]))
    # 가장 앞에 있는 먹이를 먹고 위치/이동거리 저장
    yy, xx, cc = tmp[0]
    # 먹은 물고기 제거
    fs[mp[yy][xx]] -= 1
    # 경험치 증가
    exp += 1
    # 해당 위치에 상어 위치
    mp[yy][xx] = 9
    # 상어 위치 재정립
    sk = deque([(yy, xx, cc)])
    # 크기 커지는지 확인
    if exp == sl: sl += 1; exp = 0
print(sk[0][2])