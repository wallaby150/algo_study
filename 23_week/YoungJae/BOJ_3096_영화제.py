# from itertools import combinations as cb
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# # 뱃길 저장용 딕셔너리 rd, set로 넣어서 순서 신경 안쓰게
# rd = {i: set() for i in range(1, n+1)}
# for _ in range(m):
#     a, b = map(int, input().split())
#     rd[a].add(b)
# rst = 0
# # 좌측에서 마을 2개 골라서 경우의 수 계산
# for a, b in list(cb(range(1, n+1), 2)):
#     # 두 마을이 공통으로 갈 수 있는 우측 마을 수 lrd
#     lrd = len(rd[a] & rd[b])
#     # 좌측이 고정됐을 때 가능한 개최 경우의 수 : lrd C 2
#     if lrd > 1: rst += (lrd * (lrd - 1)) // 2
# print(rst)

from itertools import combinations as cb
import sys
input = sys.stdin.readline

mx = 1 << 20
one = [0] * mx
for i in range(mx): one[i] = (i & 1) + one[i >> 1]

n, m = map(int, input().split())
tw = [0]*n
k = n // 20 + 1
for i in range(n): tw[i] = [0]*k
for _ in range(m):
    a, b = map(int, input().split())
    tw[a-1][(b-1) // 20] |= (1 << (b-1) % 20)

rst = 0
for a, b in list(cb(range(n), 2)):
    c = 0
    for l in range(k): c += one[tw[a][l] & tw[b][l]]
    rst += (c * (c - 1)) // 2
print(rst)