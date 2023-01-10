from collections import defaultdict as dt, deque
import sys
input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())
    r, c = h + 2, w + 2
    # 기존 맵 사이드에 . 추가
    mp = [['.'] * c]
    # 문 저장 딕셔너리 dr
    dr = dt(list)
    for i in range(1, h +1):
        mp.append(list('.' + input() + '.'))
        for j in range(1, w + 1):
            # 문 잇으면 dr에 추가
            if 'A' <= mp[i][j] <= 'Z': dr[mp[i][j]].append((i, j))
    mp.append(['.'] * c)
    # 열쇠 관리
    ky = list(input())
    # 열쇠가 있으면 문들 다 열어줌
    if ky != ['0']:
        for k in ky:
            for i, j in dr[k.upper()]: mp[i][j] = '.'
    # 방문 처리용 vs
    vs = [[1] * c for _ in range(r)]
    q = deque([(0, 0)])
    rs = 0
    # BFS
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < r and 0 <= nx < c and vs[ny][nx]:
                # 벽이면 그대로 진행
                if mp[ny][nx] == '*': continue
                # 방문처리
                vs[ny][nx] = 0
                # 문이 있으면 일단 그대로 진행
                if 'A' <= mp[ny][nx] <= 'Z': continue
                # 돈 발견하면 rs + 1
                if mp[ny][nx] == '$': rs += 1
                # 열쇠 발견하면 문 다 열기
                elif 'a' <= mp[ny][nx] <= 'z':
                    for i, j in dr[mp[ny][nx].upper()]:
                        mp[i][j] = '.'
                        # 발견하고 지나친 문 있었으면 queue에 추가
                        if not vs[i][j]: q.append((i, j))
                q.append((ny, nx))
    print(rs)