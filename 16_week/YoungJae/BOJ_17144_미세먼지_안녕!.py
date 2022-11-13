import sys
input = sys.stdin.readline

# 미세먼지 확산
def dust():
    # 이동되는 먼지 기록용 np
    np = [[0] * c for _ in range(r)]
    # 미세먼지 양이 5 이상이 아니면 확산되지 않음
    for y in range(r):
        for x in range(c):
            if mp[y][x] >= 5:
                a = mp[y][x] // 5
                # 확산 횟수 저장용 dc
                dc = 0
                # 상하좌우에 확산
                if y > 0 and mp[y-1][x] >= 0: np[y-1][x] += a; ac += 1
                if y < r-1 and mp[y+1][x] >= 0: np[y+1][x] += a; ac += 1
                if x > 0 and mp[y][x-1] >= 0: np[y][x-1] += a; ac += 1
                if x < c-1 and mp[y][x+1] >= 0: np[y][x+1] += a; ac += 1
                # 확산된만큼 제거
                mp[y][x] -= dc * a
    # np 값을 기존 map에 저장
    for i in range(r):
        for j in range(c):
            mp[i][j] += np[i][j]
# 공기청정기 회전
def spin():
    # 상단 회전
    for y in range(ac-3, -1, -1): mp[y+1][0] = mp[y][0]
    for x in range(c-1): mp[0][x] = mp[0][x+1]
    for y in range(ac-1): mp[y][c-1] = mp[y+1][c-1]
    for x in range(c-1, 0, -1): mp[ac-1][x] = mp[ac-1][x-1]
    # 하단 회전
    for y in range(ac+1, r-1): mp[y][0] = mp[y+1][0]
    for x in range(c-1): mp[r-1][x] = mp[r-1][x+1]
    for y in range(r-1, ac, -1): mp[y][c-1] = mp[y-1][c-1]
    for x in range(c-1, 0, -1): mp[ac][x] = mp[ac][x-1]
    # 공기청정기 우측은 0
    mp[ac-1][1] = mp[ac][1] = 0

r, c, t = map(int, input().split())
mp = []
# map 추가, 공기청정기 위치 ac에 저장
for i in range(r):
    mp.append(list(map(int, input().split())))
    if mp[i][0] == -1: ac = i
# t초동안 반복
for _ in range(t):
    dust()
    spin()
# 공기청정기 구간이 2이기 때문에 2를 더해놓고 합산
rst = 2
for x in range(r): rst += sum(mp[x])
print(rst)