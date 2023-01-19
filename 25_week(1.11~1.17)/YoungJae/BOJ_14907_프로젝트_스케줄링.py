# 자손, 부모노드 수, 시간, 결과
sn = [[] for _ in range(26)]
pr = [0] * 26
tm = [0] * 26
rs = [0] * 26

while 1:
    try:
        a, *x = input().split()
        a = ord(a) - 65
        # 시간, 자손, 부모 추가
        tm[a] = int(x[0])
        if len(x) > 1:
            for b in x[1]:
                y = ord(b) - 65
                sn[y].append(a)
                pr[a] += 1
    except: break

# 위상정렬
q = []
# 초기값 추가
for i in range(26):
    if not pr[i] and tm[i]: q.append(i)
while q:
    x = q.pop()
    rs[x] += tm[x]
    for i in sn[x]:
        rs[i] = max(rs[i], rs[x])
        pr[i] -= 1
        if not pr[i]: q.append(i)
print(max(rs))