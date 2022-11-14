from collections import deque

n = int(input())
# 시간 tm, 선생설치 pr, 최종 결과 rst
tm = [0]
pr = [[] for _ in range(n+1)]
rst = [0]*(n+1)
for i in range(1, n+1):
    l = list(map(int, input().split()))
    # 시간을 tm에 추가
    tm.append(l[0])
    # 나머지를 pr에 추가
    for j in range(1, len(l)-1):
        pr[i].append(l[j])
# queue 생성
q = deque([])
# 위상정렬 위한 while문
while 1:
    # 선행설치가 없는 것들을 queue에 추가
    for i in range(1, n+1):
        if not pr[i]: q.append(i)
    # queue에 아무것도 없으면 종료
    if len(q) == 0: break
    # queue 실행
    while q:
        x = q.pop()
        # x 건물 설치시간 추가
        rst[x] += tm[x]
        # x를 선행하는 건물들 rst에 시간 추가, 선행됐으므로 pr에서 제거
        for i in range(1, n+1):
            if x in pr[i]: pr[i].remove(x); rst[i] = max(rst[i], rst[x])
        # 이미 완료된건 -1을 넣어서 not pr이 true([])가 되지 않도록 처리
        pr[x] = [-1]
print(*rst[1:])