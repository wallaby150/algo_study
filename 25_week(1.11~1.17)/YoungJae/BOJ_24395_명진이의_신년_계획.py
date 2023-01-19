import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 51 × 51 DP 공간 생성
dp = [[-1] * 51 for _ in range(51)]
dp[0][0] = 0
for _ in range(m):
    r, b, d = map(int, input().split())
    # 이미 있는 곳에 해당 약 추가하여 위험도 추가
    # 정방향으로 가면 자가복제가 되기 때문에 역방향으로 탐색
    for i in range(50, r - 1, -1):
        for j in range(50, b - 1, -1):
            if dp[i - r][j - b] == -1: continue
            dp[i][j] = max(dp[i][j], dp[i - r][j - b] + d)
ls = []
# 학생 위험도 확인
for i in range(1, n + 1):
    x, y = map(int, input().split())
    ls.append((max(dp[x][y], 0), i))
# 정렬 후 출력
for a in sorted(ls):
    print(f'{a[1]} {a[0]}')