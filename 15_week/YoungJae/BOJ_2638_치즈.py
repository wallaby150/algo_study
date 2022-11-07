from collections import deque

# 델타 탐색
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
mp = []
# 남아있는 치즈 개수, 최종 출력 일수 CheeZe, ReSulT
cz, rst = 0, 0

# 맵 정보 가져오면서 cz 개수 확인
for i in range(n):
    mp.append(list(map(int, input().split())))
    for j in range(m):
        if mp[i][j]: cz += 1

# 치즈가 사라질 때까지 반복
while cz:
    # 하루가 지났기 때문에 rst += 1
    rst += 1
    # 방문 여부 체크 vs
    vs = [[1]*m for _ in range(n)]
    # 0,0에서 시작할거기 때문에 0으로 vs 체크
    vs[0][0] = 0
    # 녹은 치즈 저장용 MelT
    mt = set()
    # queue에 0,0 좌표 입력
    q = deque([(0, 0)])
    # BFS
    while q:
        y, x = q.popleft()
        # 델타 탐색
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            # 맵 안이고 방문한 적 없으면
            if 0 <= ny < n and 0 <= nx < m and mp[ny][nx] >= 0 and vs[ny][nx]:
                # 치즈가 있으면 vs에 1 추가
                # 3 이상(=2 초과)이면 두 면 이상 닿은 것이기 때문에 mt에 추가
                # 치즈 내부 공기는 BFS로 인해 방문을 못하기 때문에 괜찮다
                if mp[ny][nx]:
                    vs[ny][nx] += 1
                    if vs[ny][nx] > 2: mt.add((ny, nx))
                # 치즈가 아니면 vs 체크 후 queue에 추가
                else:
                    vs[ny][nx] = 0
                    q.append((ny, nx))
    # 녹은 치즈들 지워주고 남은 치즈 개수 줄이기
    for y, x in mt: mp[y][x] = 0; cz -= 1
print(rst)