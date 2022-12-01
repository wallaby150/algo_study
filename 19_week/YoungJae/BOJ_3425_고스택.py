# 계산 함수 calc
def calc(mr, n):
    st = [n]
    # 각 명령어에 따라 계산
    for m in mr:
        # NUM이면 뒤의 숫자 stack에 추가
        if m[:3] == 'NUM': st.append(int(m[4:]))
        # 이후 연산은 stack이 비어있으면 불가
        elif not st: return 'ERROR'
        elif m == 'POP': st.pop()
        elif m == 'INV': st[-1] = -st[-1]
        elif m == 'DUP': st.append(st[-1])
        # 이후 연산은 stack에 값이 2개 이상 있어야 가능
        elif len(st) < 2: return 'ERROR'
        elif m == 'SWP': st[-1], st[-2] = st[-2], st[-1]
        # 2개간의 연산의 경우 x,y를 꺼내 계산
        else:
            x, y = st.pop(), st.pop()
            # 합/차/곱은 연산범위 벗어나는지 확인
            if m == 'ADD' and abs(x+y) <= 1e9: st.append(x + y)
            elif m == 'SUB' and abs(y-x) <= 1e9: st.append(y - x)
            elif m == 'MUL' and abs(x*y) <= 1e9: st.append(x * y)
            # 몫/나머지는 x가 0이면 계산 불가
            elif x == 0: return 'ERROR'
            # 몫은 둘 중 하나만 음수이면 음수, 아니면 양수
            elif m == 'DIV':
                if (x > 0) == (y > 0): st.append(abs(y) // abs(x))
                else: st.append(-(abs(y) // abs(x)))
            # 나머지는 y만 보고 따짐
            elif m == 'MOD':
                if y > 0: st.append(abs(y) % abs(x))
                else: st.append(-(abs(y) % abs(x)))
            else: return 'ERROR'
    # 최종 결과에 스택이 하나가 아니면 에러
    if len(st) != 1: return 'ERROR'
    else: return st[0]

while 1:
    mr = []
    # 명령어 입력
    while 1:
        a = input()
        if a == 'QUIT': quit()
        if a == 'END': break
        mr.append(a)
    n = int(input())
    for _ in range(n): print(calc(mr, int(input())))
    # 입력/출력 둘 다 한 줄 비워있으므로 input/print 한 번씩
    input()
    print()