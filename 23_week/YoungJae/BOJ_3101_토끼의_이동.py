# 방향에 따른 좌표 이동
dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
n, k = map(int, input().split())
ls = list(input())
# 각 대각줄의 길이 ln, 각 대각줄의 최대값 sm
ln = list(range(n)) + list(range(n-2, -1, -1))
sm = [1]
for i in range(1, len(ln)): sm.append(sm[i-1] + ln[i] + 1)

# 시작점 (0,0), cnt 1
y = x = 0
cnt = 1
# 이동 명령
for d in ls:
    # 이동에 따라 x,y 좌표 이동
    y += dr[d][0]; x += dr[d][1]
    # s, c 좌표 계산
    s = y + x
    # 0 ~ n-1까지는 c는 x좌표랑 동일
    # 그보다 커지면 커짐에 따라 좌우로 1칸씩은 행렬 밖으로 벗어남
    # c 좌표는 좌하단부터만 계산하기 때문에 좌측 1칸씩만 빼는 것이므로 x - (s - (n - 1))로 계산
    if s < n: c = x
    else: c = x + n - 1 - s
    # s가 홀수면 좌하단으로 갈수록 커지므로 최대값 - c
    # 짝수면 우상단으로 갈수록 커지므로 최소값(sm - ln)에 c 좌표 추가
    if s % 2: ss = sm[s] - c
    else: ss = sm[s] - ln[s] + c
    cnt += ss
print(cnt)