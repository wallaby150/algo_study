from collections import deque

n, m = map(int, input().split())
# 사다리, 뱀 저장용 ld, bm
ld, bm = {}, {}
# 사다리 저장
for _ in range(n):
    a, b = map(int, input().split())
    ld[a] = b
# 뱀 저장
for _ in range(m):
    a, b = map(int, input().split())
    bm[a] = b
# 맵, 방문여부 mp, vs
mp = [0]*101
vs = [0]*101
# queue
q = deque([(1, 0)])
vs[1] = 1
# BFS
while q:
    x, c = q.popleft()
    if x == 100 : break
    # 주사위 눈금 1~6까지
    for i in range(1, 7):
        xx = x + i
        # 사다리/뱀 태우기
        if xx in ld : xx = ld[xx]
        if xx in bm : xx = bm[xx]
        # 게임판 안이고 방문한 적 없으면 방문까지 걸린 횟수 기록, queue에 추가
        if xx <= 100 and not vs[xx]: vs[xx] = c+1; q.append((xx, c+1))
print(vs[-1])