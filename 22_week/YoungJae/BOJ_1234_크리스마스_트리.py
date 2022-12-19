from math import factorial as f

# DFS, 현재 레벨 m, 남은 장난감 개수 rr, gg, bb
def dfs(m, rr, gg, bb):
    # 레벨 끝이면 1 출력
    if m > n: return 1
    # DP: 이미 있으면 DFS 대신 불러오기
    if dp[m][rr][gg][bb] != -1: return dp[m][rr][gg][bb]
    c = 0
    # 0 ~ (m, rr 중 최솟값)까지 반복
    for i in range(min(m, rr)+1):
        # 0 ~ (m-i, gg 중 최솟값)까지 반복
        for j in range(min(m-i, gg)+1):
            # 나머지 채워야 할 장난감을 k로 채움
            k = m-i-j
            # k가 음수거나 가진 개수보다 많으면 패스
            if k > bb or k < 0: continue
            # 들어가는 장난감 색이 동일한지 확인
            # 0 아닌 것들만 tt에 넣은 뒤 최댓값 최솟값 같은지 확인
            tt = []
            for t in [i, j, k]:
                if t: tt.append(t)
            if max(tt) != min(tt): continue
            # 조건을 만족하면 다음 레벨 값 추가
            # 장난감 배치 경우의 수 (r+g+b)!/r!g!b! 곱해줘야 함
            c += dfs(m+1, rr-i, gg-j, bb-k) * f(i+j+k)//(f(i)*f(j)*f(k))
    # DP에 저장
    dp[m][rr][gg][bb] = c
    return c

n, r, g, b = map(int, input().split())
dp = [[[[-1]*56 for _ in range(56)] for _ in range(56)] for _ in range(n+1)]
print(dfs(1, r, g, b))