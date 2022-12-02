# https://www.acmicpc.net/problem/1484
import sys
sys.stdin = open('input.txt')

G = int(sys.stdin.readline())

result = []
a = 2       # 현재 몸무게
while True:
    if a**2 - (a-1)**2 > G:     # 두 수의 제곱 차가 G보다 크면 중지
        break

    b = 1       # 이전 몸무게
    while b < a:        # 조건을 만족하는 몸무게 찾기
        if a**2 - b**2 == G:
            result.append(a)
            break

        b += 1

    a += 1

if result:
    for i in result:
        print(i)
else:
    print(-1)