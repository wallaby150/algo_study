# https://www.acmicpc.net/problem/6588

import sys

sys.stdin = open('input.txt')

# 소수는 1, 아니면 0
number = [1] * 1000001
number[0], number[1] = 0, 0
n = 1

# number[i] == 1 인 가장 작은 수는 소수, 해당 수의 배수는 소수에서 제외
# 에라토스테네스의 채
while n < 500000:
    n += 1
    if number[n] == 1:
        for i in range(n, 1000001, n):
            number[i] = 0
        number[n] = 1

# 가장 작은 소수부터 조건 만족하는지 검사
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    for i in range(2, 1000001):
        if number[i] == 1:
            if number[num - i] == 1:
                print(f'{num} = {i} + {num - i}')
                break