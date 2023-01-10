# DFS
def dfs(x, c, r):
    global rst
    # 다 돌았으면 기존 값과 비교해 작은 값 저장
    if c == n:
        if rst > r: rst = r
        return
    # 이미 초과했으면 종료
    if r > rst: return
    # 순차적으로 돌면서 DFS
    for i in range(n):
        if vs[i]:
            vs[i] = 0
            dfs(i, c + 1, r + mp[x][i])
            # 백트래킹 위해 다시 vs 초기화
            vs[i] = 1

n, k = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
# 워셜-플로이드
for l in range(n):
    for i in range(n):
        for j in range(n):
            if mp[i][j] > mp[i][l] + mp[l][j]: mp[i][j] = mp[i][l] + mp[l][j]
vs = [1] * n
vs[k] = 0
rst = 1e9
dfs(k, 1, 0)
print(rst)