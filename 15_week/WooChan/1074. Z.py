'''
https://www.acmicpc.net/problem/1074

[문제]

한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다.
N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

'''
import sys

N, r, c = map(int, sys.stdin.readline().split())

# 배열을 4분면으로 나눠 위치한 분면에 따라 값을 더해준 후
# 위치한 분면을 전체 배열로 보고 다시 반복
count = -1      # [0, 0] => 0번째 이므로 count = -1 부터 시작
while N > 0:
    length = 2 ** N
    if r < length//2:
        if c < length//2:
            locate = 1      # 좌상단
        else:
            locate = 2      # 우상단
            c -= length//2
    else:
        if c < length//2:
            locate = 3      # 좌하단
            r -= length//2
        else:
            locate = 4      # 우하단
            r -= length//2
            c -= length//2
    if N == 1:      # 마지막 2*2 배열에서 위치한 분면 값을 더해준다
        count += locate
    else:       # n번째 분면일 때 (한 분면의 크기) * (n-1) 만큼 더해준다
        count += (locate-1) * ((2 ** (N-1)) ** 2)

    N -= 1      # 전체 배열의 크기 조정

print(count)