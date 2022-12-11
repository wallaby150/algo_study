n, m = map(int, input().split())
t, *tr = map(int, input().split())
tr = set(tr)
rst, ls = 0, []
for _ in range(m):
    k, *mb = map(int, input().split())
    ls.append(set(mb))
i = 0
while i < m:
    if tr & ls[i] and ls[i] - tr: tr |= ls[i]; i = 0
    else: i += 1
for a in ls:
    if not (tr & a) : rst += 1
print(rst)