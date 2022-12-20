# https://www.acmicpc.net/problem/16928
import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

board = [100] * 101
ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    snake[u] = v

stack = deque()
stack.append(1)
board[1] = 0

while stack:
    location = stack.popleft()
    for i in range(1, 7):
        next_location = location + i
        if next_location <= 100:
            if next_location in ladder.keys():
                next_location = ladder[next_location]
            elif next_location in snake.keys():
                next_location = snake[next_location]
            if board[location] + 1 < board[next_location]:
                board[next_location] = board[location] + 1
                stack.append(next_location)

print(board[100])