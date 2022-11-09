'''
https://www.acmicpc.net/problem/2109

[문제]

한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다.
각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다.
각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다.
이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다.
강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.

'''
import sys

n = int(sys.stdin.readline())

day = [[] for _ in range(10001)]
pay = []

max_day = 0
for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    day[d] = day[d] + [p]
    if d > max_day:
        max_day = d

for i in range(max_day, 0, -1):
    max_pay = 0
    go = -1
    for j in range(i, max_day+1):
        if len(day[j]) > 0 and max(day[j]) >= max_pay:
            max_pay = max(day[j])
            go = j
    if go != -1:
        pay.append(max_pay)
        day[go].remove(max_pay)

print(sum(pay))