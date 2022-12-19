import sys
sys.setrecursionlimit(10**8)

# 이동 함수, 같으면 1, 반대면 4, 0에서 움직이면 2, 나머지 3
def mv(a, b):
    if a == b: return 1
    if not a: return 2
    if not (a - b) % 2: return 4
    return 3

# DP
def lr(i, l, r):
    global dp
    # 마지막이면 종료
    if not bt[i]: return 0
    # 이미 값이 있으면 출력
    if dp[i][l][r] != -1: return dp[i][l][r]
    # 왼발 움직였을 때와 오른발 움직였을 때 중 최소값 저장
    dp[i][l][r] = min(lr(i+1, bt[i], r) + mv(l, bt[i]), lr(i+1, l, bt[i]) + mv(r, bt[i]))
    return dp[i][l][r]

bt = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(10**6)]

print(lr(0, 0, 0))