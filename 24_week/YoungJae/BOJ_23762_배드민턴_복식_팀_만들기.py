n = int(input())
# 실력 받아서 정렬 + enumerate로 idx도 저장
st = sorted(enumerate(list(map(int, input().split()))), key=lambda x: x[1])
# idx는 idx에, 실력은 pl에 저장
idx = []; pl = []
for i, x in st: idx.append(i); pl.append(x)
# i-3 ~ i번째 4명을 한 팀으로 모았을 때 실력차 sm
sm = [1e9] * n
for i in range(3, n): sm[i] = pl[i] - pl[i - 3]
# 깍두기 리스트 ls
ls = [[0], [0, 1], [0, 1, 2], []]
# i번째까지 실력차 합 최소값 DP[i]
dp = [0] * n
# DP[3]은 4명만 있으므로 sm[3]과 동일
dp[3] = sm[3]
# DP
for i in range(4, n):
    # 나머지가 3이면 모두 4명씩 묶이기 때문에 dp는 dp[i-4]에 마지막 4명 합
    if i % 4 == 3: dp[i] = dp[i - 4] + sm[i]; ls.append([])
    else:
        # i-1번째 결과에 i번째 사람은 빠지는 경우 : dp[i - 1]
        # i-4번째 값에 4명이 팀을 짰을 경우 : dp[i - 4] + sm[i]
        # 전자가 더 작으면 리스트에는 ls[i - 1]에 i만 추가
        # 후자가 더 작으면 ls[i - 4] 그대로 유지
        if dp[i - 1] < dp[i - 4] + sm[i]:
            dp[i] = dp[i - 1]; ls.append(ls[i - 1] + [i])
        else: dp[i] = dp[i - 4] + sm[i]; ls.append(ls[i - 4]) 
print(dp[-1])
for a in ls[-1]: print(idx[a])