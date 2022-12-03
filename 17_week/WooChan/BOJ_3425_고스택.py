# https://www.acmicpc.net/problem/3425
import sys
from collections import deque
sys.stdin = open('input.txt')

theEnd = 0

while True:
    tasks = []

    while True:
        order = sys.stdin.readline().strip()

        if order == 'QUIT':
            theEnd = 1
            break
        if len(order) > 3:
            tasks.append(list(map(str, order.split())))
        elif order == 'END':
            break
        else:
            tasks.append(order)

    if theEnd == 1:
        break

    N = int(sys.stdin.readline().strip())
    error = 0
    for case in range(N):
        stack = deque()
        stack.append(int(sys.stdin.readline().strip()))
        end = 0
        if error == 1:
            print('ERROR')
            end = 1
        else:
            for task in tasks:
                if type(task) == list:
                    stack.append(int(task[1]))
                else:
                    if not stack:
                        print('ERROR')
                        end = 1
                        break
                    if task == 'POP':
                        stack.pop()
                    elif task == 'INV':
                        stack[-1] = -stack[-1]
                    elif task == 'DUP':
                        stack.append(stack[-1])
                    else:
                        if len(stack) < 2:
                            print('ERROR')
                            end = 1
                            break
                        if task == 'SWP':
                            stack[-1], stack[-2] = stack[-2], stack[-1]
                        elif task == 'ADD':
                            stack[-2] = stack[-2] + stack[-1]
                            if stack[-2] > 10**9 or stack[-2] < -(10**9):
                                print('ERROR')
                                end = 1
                                break
                            stack.pop()
                        elif task == 'SUB':
                            stack[-2] = stack[-2] - stack[-1]
                            if stack[-2] > 10**9 or stack[-2] < -(10**9):
                                print('ERROR')
                                end = 1
                            stack.pop()
                        elif task == 'MUL':
                            stack[-2] = stack[-2] * stack[-1]
                            if stack[-2] > 10**9 or stack[-2] < -(10**9):
                                print('ERROR')
                                end = 1
                                break
                            stack.pop()
                        elif task == 'DIV':
                            minus = 0
                            if stack[-1] < 0:
                                stack[-1] = -stack[-1]
                                minus += 1
                            if stack[-2] < 0:
                                stack[-2] = -stack[-2]
                                minus += 1
                            if stack[-1] == 0:
                                print('ERROR')
                                end = 1
                                break
                            else:
                                stack[-2] = stack[-2] // stack[-1]
                                if minus == 1:
                                    stack[-2] = -stack[-2]
                                stack.pop()
                        elif task == 'MOD':
                            minus = 0
                            if stack[-1] < 0:
                                stack[-1] = -stack[-1]
                            if stack[-2] < 0:
                                stack[-2] = -stack[-2]
                                minus = 1
                            if stack[-1] == 0:
                                print('ERROR')
                                end = 1
                                break
                            else:
                                stack[-2] = stack[-2] % stack[-1]
                                if minus == 1:
                                    stack[-2] = -stack[-2]
                                stack.pop()

        if end == 0:
            if len(stack) != 1:
                print('ERROR')
            else:
                print(stack.pop())

    space = sys.stdin.readline()
    print()