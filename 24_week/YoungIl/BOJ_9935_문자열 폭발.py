import sys

txt = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
stack = []
length = len(target)
target_list = list(target)

for char in txt:
    stack.append(char)
    # replace가 아니라 stack을 써야 했다.
    if stack[-length:] == target_list:
        stack[:-length] = []
        # 범위 잘 정해주기

if stack:
    print("".join(stack))
else:
    print("FRULA")