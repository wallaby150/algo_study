import sys
from collections import  deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 격자크기 2**N
# 파이어스톰 시전 횟수 Q번
N, Q = map(int,input().split())
A = [list((map(int,input().split()))) for _ in range(2**N)]
# 시전 단계 순서
Ls = tuple(map(int,input().split()))

di,dj = [0,0,1,-1],[1,-1,0,0]

for L in Ls:
    LL = 2**L
    i,j = 0, 0
    for i in range(0,2**N,LL):
        if (i//2)%2 == 0:
            for j in range(0,2**N,LL):
                # 격자 스왑
                LLs_nums = []
                for ii in range(i,i+LL):
                    for jj in range(j,j+LL):
                        LLs_nums.append(A[ii][jj])

                LLs_idx = 0
                for jj in range(j + LL -1,j -1,-1):
                    for ii in range(i, i + LL):
                        A[ii][jj] = LLs_nums[LLs_idx]
                        LLs_idx += 1

        elif (i//2)%2 == 1:
            for j in range(0,2**N,LL):
                # 격자 스왑
                LLs_nums = []
                for ii in range(i, i + LL):
                    for jj in range(j, j + LL):
                        LLs_nums.append(A[ii][jj])

                LLs_idx = 0
                for jj in range(j + LL -1, j -1, -1):
                    for ii in range(i, i + LL):
                        A[ii][jj] = LLs_nums[LLs_idx]
                        LLs_idx += 1

    ice_boxs = []
    for i in range(0,2**N):
        for j in range(0,2**N):
            ice_box = 0
            for k in range(0,4):
                dii, djj = i + di[k], j + dj[k]
                if 0<=dii<2**N and 0<=djj<2**N and A[dii][djj] > 0:
                    ice_box += 1
            if ice_box < 3 and A[i][j] > 0 :
                ice_boxs.append((i,j))

    for ib in ice_boxs:
        i,j = ib
        A[i][j] -= 1

# 합 / 가장 큰 덩어리의 칸 개수
sums = 0
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
q = deque()
max_box = 0
for i in range(0,2**N):
    for j in range(0,2**N):
        sums += A[i][j]

for i in range(0, 2 ** N):
    for j in range(0, 2 ** N):
        if A[i][j] > 0:
            q.append((i,j))
            this_box = 0
            while q:
                i, j = q.popleft()
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    this_box += 1
                    for k in range(0, 4):
                        dii, djj = i + di[k], j + dj[k]
                        if 0 <= dii < 2 ** N and 0 <= djj < 2 ** N and A[dii][djj] > 0:
                            q.append((dii,djj))
            max_box = max(max_box, this_box)

print(sums)
print(max_box)

