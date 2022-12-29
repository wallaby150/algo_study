# Union-Find
def fnd(x):
    if x == pr[x]: return x
    pr[x] = fnd(pr[x])
    return pr[x]

def uni(x, y):
    x, y = fnd(x), fnd(y)
    if x < y: pr[y] = x
    else: pr[x] = y

n, m = int(input()), int(input())
pr = list(range(n))
# 연결 정보 따라 Union 작업
for i in range(n):
    rt = list(map(int, input().split()))
    # 대각행렬이므로 우상단만 확인
    for j in range(i+1, n):
        if rt[j]: uni(i, j)
pl = list(map(int, input().split()))
# 부모성분 다시 찾아주기
for i in range(n): pr[i] = fnd(pr[i])
# i에 맞추기 위해 0번 추가
pr = [0] + pr
bg = pr[pl[0]]
# 출발점과 부모가 다른 도착지 있으면 NO 없으면 YES
for p in pl:
    if pr[p] != bg: print('NO'); break
else: print('YES')