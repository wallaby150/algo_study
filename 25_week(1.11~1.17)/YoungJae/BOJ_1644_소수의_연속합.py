n = int(input())
# 소수 체 nm, 소수 목록 pn
nm = [1]*(n+1)
pn = [2]
# 에라토스테네스의 체
for j in range(4, n+1, 2): nm[j] = 0
for i in range(3, n+1, 2):
    if nm[i]:
        pn.append(i)
        for j in range(i*2, n+1, i): nm[j] = 0
rst = s = e = 0
# 포인터로 체크
while e <= len(pn):
    sm = sum(pn[s:e])
    if sm == n: rst += 1
    # 합이 목표값보다 작으면 뒷값을, 크면 앞값을 더함
    if sm < n: e += 1
    else: s += 1
print(rst)