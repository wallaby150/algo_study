x = list(input())
p = list(input())
n = len(p)
# 스택
st = []
for a in x:
    # 스택에 문자 추가
    st.append(a)
    # 스택 마지막이 폭발 문자열이면 폭발
    if st[-n:] == p:
        for i in range(n): st.pop()
# 스택이 최종적으로 전부 비었으면 FRULA
if len(st) == 0: print('FRULA')
else: print(''.join(st))