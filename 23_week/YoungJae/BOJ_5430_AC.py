from collections import deque

t = int(input())
for tc in range(t):
    p = input()
    n = int(input())
    x = deque(input()[1:-1].split(','))
    if n == 0 : x = deque()
    chk = 0
    rn = 0
    # 함수 실행
    for a in p:
        # R이면 뒤집기 : 뒤집진 앟고 횟수만 체크
        if a == 'R': rn += 1
        # D이면 첫 수 버리기
        # 비어있으면 error 출력 / 바로 끝내기 위해 chk 확인
        if a == 'D':
            if not x:print('error');chk = 1;break
            # 뒤집힌 횟수 따라 앞/뒤 버리기
            else:
                if not rn % 2: x.popleft()
                else: x.pop()
    if chk: continue
    if rn % 2: x.reverse()
    print(f'[{",".join(x)}]')