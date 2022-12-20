# 회전 함수
def spin(l):
    # 저장용 t
    t = [[] for _ in range(n)]
    # 작은 격자 불러오기
    for i in range(0, n, l):
        for j in range(0, n, l):
            # 격자 저장용 tp
            tp = []
            for k in range(i, i+l): tp.append(mp[k][j:j+l])
            # tp 회전
            # zip(*tp): tp의 i번째끼리 묶음
            tp = [list(reversed(z)) for z in zip(*tp)]
            # 회전한걸 t에 저장
            for k in range(i+l-1, i-1, -1): t[k] += tp.pop()
    return t

# 얼음 녹이는 함수
def melt():
    # mp와 같은 tp
    tp = [a[:] for a in mp]
    for i in range(n):
        for j in range(n):
            # 얼음 없으면 패스
            if not mp[i][j]: continue
            c = 4
            # 상하좌우에 얼음 없거나 맵 밖이면 c 줄임
            if i > n-2 or not mp[i+1][j]: c -= 1
            if i < 1 or not mp[i-1][j]: c -= 1
            if j > n-2 or not mp[i][j+1]: c -= 1
            if j < 1 or not mp[i][j-1]: c -= 1
            # 3 미만이면 얼음 녹음
            if c < 3: tp[i][j] -= 1
    return tp

# DFS
def dfs(st):
    # 기본 count 1
    c = 1
    while st:
        y, x = st.pop()
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + d[0], x + d[1]
            # 범위 내고 방문 없고 얼음 있으면 방문표시, count 증가, 스택 추가
            if 0 <= ny < n and 0 <= nx < n and vs[ny][nx] and mp[ny][nx]:
                vs[ny][nx] = 0; c += 1; st.append((ny, nx))
    return c

n, q = map(int, input().split())
# 2ⁿ만 쓰므로 변경
n = 2**n
mp = [list(map(int, input().split())) for _ in range(n)]
m = list(map(int, input().split()))

# 주문 따라 회전하고 녹임
# 0일 땐 spin 발생 안하게 처리해서 시간 단축
for l in m:
    if l: mp = spin(2**l)
    mp = melt()

# 합산, 덩어리 계산 sm, cnt
sm = cnt = 0
vs = [[1]*n for _ in range(n)]
# 행마다 합산 계산, 각 좌표마다 덩어리 계산
for i in range(n):
    sm += sum(mp[i])
    for j in range(n):
        if vs[i][j] and mp[i][j]:
            vs[i][j] = 0
            cnt = max(cnt, dfs([(i, j)]))
print(sm)
# 덩어리 없으면 0 출력
if cnt != 1: print(cnt)
else: print(0)