n = int(input())
dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]
mp = [list(map(int, input().split())) for _ in range(n)]
# 각 방향 회전에 맞춰 좌표와 퍼센트 적어두는 리스트
lf = [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1),
      (2, 0, 2), (1, -1, 10), (1, 0, 7), (1, 1, 1), (0, -2, 5)]
rt = [(y, -x, p) for y, x, p in lf]
up = [(x, y, p) for y, x, p in lf]
dn = [(-x, y, p) for y, x, p in lf]
# 방향에 맞춰 불러올 딕셔너리 dr
dr = {0: lf, 1: dn, 2: rt, 3: up}

# 방향 d, 횟수 c, 반복횟수 r, 최대횟수 m
d, c, r, m = 0, 0, 0, 1
# 중앙에서 시작
y = x = n//2
rst = 0
while 1:
    # 이동 후 범위 밖으로 벗어나면 종료
    y += dy[d]; x += dx[d]
    if not 0 <= y < n or not 0 <= x < n: break
    # 모래 가져오기, 잔여 모래 저장용 ns
    s = mp[y][x]; mp[y][x] = 0
    ns = s
    # 모래 흩뿌리기
    for yy, xx, p in dr[d]:
        if 0 <= y+yy < n and 0 <= x+xx < n:
            mp[y+yy][x+xx] += s * p // 100
        else: rst += s * p // 100
        ns -= s * p // 100
    # 남은 모래 옮기기
    if 0 <= y+dy[d] < n and 0 <= x+dx[d] < n:
        mp[y+dy[d]][x+dx[d]] += ns
    else: rst += ns
    # 다음 방향 조정
    # m번 d방향으로 움직였으면 r 증가, 다음 방향으로
    # r이 2가 되면 m 1 증가
    c += 1
    if c == m: r += 1; d = (d + 1) % 4; c = 0
    if r > 1: r = 0; m += 1
print(rst)