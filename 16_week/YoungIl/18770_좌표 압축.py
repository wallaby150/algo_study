n = int(input())
dots = list(map(int, input().split()))

enu_dots = []
for i, v in enumerate(dots):
    enu_dots.append([i, v])         # 해당 리스트에 enumerate 항목을 리스트로 다시 추가해준다.

sorted_enu_dots = sorted(enu_dots, key = lambda x : x[1])       # value 기준으로 정렬해준다.

count = 0                                                       # 각각의 값이 가지는 번호를 기록할 변수
now = sorted_enu_dots[0][1]                                     # 첫 값은 정렬된 리스트의 첫번째 값의 value

for dot in sorted_enu_dots:         # 정렬된 값을 순회하면서
    if dot[1] == now:               # 같은 값이었으면
        dot.append(count)           # [idx, value]에 번호를 추가해서 넣어준다.
    else:
        count += 1                  # 더 큰 값이면 count += 1
        dot.append(count)
        now = dot[1]

for j in sorted(sorted_enu_dots):       # 다시 idx 기준으로 정렬
    print(j[2], end=' ')                # idx 순으로 순회하면서 각각의 리스트에 저장된 count값을 출력한다.