# https://www.acmicpc.net/problem/10026

import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

picture = [list(map(str, sys.stdin.readline())) for _ in range(N)]

count_normal = 0
count_color = 0

stack_normal = deque()
stack_color = deque()
visited_normal = [[0] * N for _ in range(N)]
visited_color = [[0] * N for _ in range(N)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    for j in range(N):
        if visited_normal[i][j] == 0:
            stack_normal.append((i, j, picture[i][j]))
            visited_normal[i][j] = 1
            count_normal += 1

        while stack_normal:
            x, y, color = stack_normal.pop()
            for d in range(4):
                next_x = x + direction[d][0]
                next_y = y + direction[d][1]
                if 0 <= next_x < N and 0 <= next_y < N:
                    if picture[next_x][next_y] == color and visited_normal[next_x][next_y] == 0:
                        stack_normal.append((next_x, next_y, color))
                        visited_normal[next_x][next_y] = 1


        if visited_color[i][j] == 0:
            stack_color.append((i, j, picture[i][j]))
            visited_color[i][j] = 1
            count_color += 1
        while stack_color:
            x, y, color = stack_color.pop()
            for d in range(4):
                next_x = x + direction[d][0]
                next_y = y + direction[d][1]
                if 0 <= next_x < N and 0 <= next_y < N and visited_color[next_x][next_y] == 0:
                    if color == 'R' or color == 'G':
                        if picture[next_x][next_y] == 'R' or picture[next_x][next_y] == 'G':
                            stack_color.append((next_x, next_y, color))
                            visited_color[next_x][next_y] = 1
                    else:
                        if picture[next_x][next_y] == color and visited_color[next_x][next_y] == 0:
                            stack_color.append((next_x, next_y, color))
                            visited_color[next_x][next_y] = 1

print(count_normal, count_color)