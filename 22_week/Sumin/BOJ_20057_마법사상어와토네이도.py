import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 왼 아래 오른 위 ...
di, dj = [0,1,0,-1] , [-1,0,1,0]

# N은 홀수만 주어진다
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)

# start 시작점. 0 ~ N-1 이므로 중간은 N//2
start = (N//2,N//2)

# turn마다 왼, 아래는 turn만큼. 오른, 위는 turn+1 만큼 이동한다
# 한 턴이 종료되면 turn이 2씩 증가하며, 왼쪽으로 N-1 만큼 가는 시점에서 종료된다
turn = 1

# dir 왼0 아래1 오른2 위3
# 각 방향에 대해 모래의 이동 결과를 다르게 반영
dir = 0

# 범위 밖으로 나간 모래
result = 0

i, j = start
while (i,j) != (0,0):
    for d in range(0,4):
        if d in (0,1) :
            for t in range(1,turn+1):
                if d == 0: # 왼
                    dii, djj = i + di[d], j + dj[d]
                    if 0 <= dii < N and 0 <= djj < N:
                        sand = arr[dii][djj]
                        asand = arr[dii][djj]
                        arr[dii][djj] = 0
                        i, j = dii, djj
                    if sand > 0 :
                        # 2%
                        if 0 <= dii -2 < N and 0 <= djj < N: arr[dii-2][djj] += int((sand * 0.02) // 1)
                        else: result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        if 0 <= dii + 2 < N and 0 <= djj < N: arr[dii + 2][djj] += int((sand * 0.02) // 1)
                        else: result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        # 7%
                        if 0 <= dii -1 < N and 0 <= djj < N: arr[dii-1][djj] += int((sand * 0.07) // 1)
                        else: result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj < N: arr[dii + 1][djj] += int((sand * 0.07) // 1)
                        else: result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        # 10%
                        if 0 <= dii -1 < N and 0 <= djj-1 < N: arr[dii-1][djj-1] += int((sand * 0.1) // 1)
                        else: result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj-1 < N: arr[dii+1][djj-1] += int((sand * 0.1) // 1)
                        else: result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        # 1%
                        if 0 <= dii -1 < N and 0 <= djj+1 < N: arr[dii-1][djj+1] += int((sand * 0.01) // 1)
                        else: result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj+1 < N: arr[dii+1][djj+1] += int((sand * 0.01) // 1)
                        else: result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        # 5%
                        if 0 <= dii + 2*di[d] < N and 0 <= djj + 2*dj[d] < N:
                            arr[dii + 2*di[d]][djj + 2*dj[d]] += int((sand * 0.05) // 1)
                        else:
                            result += int((sand * 0.05) // 1)
                        asand -= int((sand * 0.05) // 1)

                        # a%
                        if 0 <= dii + di[d] < N and 0 <= djj + dj[d] < N:
                            arr[dii + di[d]][djj + dj[d]] += asand
                        else:
                            result += asand
                elif d == 1: # 아래
                    dii, djj = i + di[d], j + dj[d]
                    if 0 <= dii < N and 0 <= djj < N:
                        sand = arr[dii][djj]
                        asand = arr[dii][djj]
                        arr[dii][djj] = 0
                        i, j = dii, djj

                    if sand > 0:
                        # 2%
                        if 0 <= dii < N and 0 <= djj-2 < N:
                            arr[dii][djj-2] += int((sand * 0.02) // 1)
                        else:
                            result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        if 0 <= dii < N and 0 <= djj+2 < N:
                            arr[dii][djj+2] += int((sand * 0.02) // 1)
                        else:
                            result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        # 7%
                        if 0 <= dii< N and 0 <= djj-1 < N:
                            arr[dii][djj-1] += int((sand * 0.07) // 1)
                        else:
                            result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        if 0 <= dii < N and 0 <= djj+1 < N:
                            arr[dii][djj+1] += int((sand * 0.07) // 1)
                        else:
                            result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        # 10%
                        if 0 <= dii + 1 < N and 0 <= djj - 1 < N:
                            arr[dii + 1][djj - 1] += int((sand * 0.1) // 1)
                        else:
                            result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj + 1 < N:
                            arr[dii + 1][djj + 1] += int((sand * 0.1) // 1)
                        else:
                            result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        # 1%
                        if 0 <= dii - 1 < N and 0 <= djj - 1 < N:
                            arr[dii - 1][djj - 1] += int((sand * 0.01) // 1)
                        else:
                            result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        if 0 <= dii - 1 < N and 0 <= djj + 1 < N:
                            arr[dii - 1][djj + 1] += int((sand * 0.01) // 1)
                        else:
                            result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        # 5%
                        if 0 <= dii + 2 * di[d] < N and 0 <= djj + 2 * dj[d] < N:
                            arr[dii + 2 * di[d]][djj + 2 * dj[d]] += int((sand * 0.05) // 1)
                        else:
                            result += int((sand * 0.05) // 1)
                        asand -= int((sand * 0.05) // 1)

                        # a%
                        if 0 <= dii + di[d] < N and 0 <= djj + dj[d] < N:
                            arr[dii + di[d]][djj + dj[d]] += asand
                        else:
                            result += asand
                if (i, j) == (0, 0):
                    break
        elif d in (2,3):
            for t in range(1,turn+2):
                if d == 2: # 오른
                    dii, djj = i + di[d], j + dj[d]
                    if 0 <= dii < N and 0 <= djj < N:
                        sand = arr[dii][djj]
                        asand = arr[dii][djj]
                        arr[dii][djj] = 0
                        i, j = dii, djj

                    if sand > 0:
                        # 2%
                        if 0 <= dii - 2 < N and 0 <= djj < N:
                            arr[dii - 2][djj] += int((sand * 0.02) // 1)
                        else:
                            result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        if 0 <= dii + 2 < N and 0 <= djj < N:
                            arr[dii + 2][djj] += int((sand * 0.02) // 1)
                        else:
                            result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        # 7%
                        if 0 <= dii - 1 < N and 0 <= djj < N:
                            arr[dii - 1][djj] += int((sand * 0.07) // 1)
                        else:
                            result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj < N:
                            arr[dii + 1][djj] += int((sand * 0.07) // 1)
                        else:
                            result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        # 10%
                        if 0 <= dii - 1 < N and 0 <= djj + 1 < N:
                            arr[dii - 1][djj + 1] += int((sand * 0.1) // 1)
                        else:
                            result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj + 1 < N:
                            arr[dii + 1][djj + 1] += int((sand * 0.1) // 1)
                        else:
                            result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        # 1%
                        if 0 <= dii - 1 < N and 0 <= djj - 1 < N:
                            arr[dii - 1][djj - 1] += int((sand * 0.01) // 1)
                        else:
                            result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj - 1 < N:
                            arr[dii + 1][djj - 1] += int((sand * 0.01) // 1)
                        else:
                            result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        # 5%
                        if 0 <= dii + 2 * di[d] < N and 0 <= djj + 2 * dj[d] < N:
                            arr[dii + 2 * di[d]][djj + 2 * dj[d]] += int((sand * 0.05) // 1)
                        else:
                            result += int((sand * 0.05) // 1)
                        asand -= int((sand * 0.05) // 1)

                        # a%
                        if 0 <= dii + di[d] < N and 0 <= djj + dj[d] < N:
                            arr[dii + di[d]][djj + dj[d]] += asand
                        else:
                            result += asand
                elif d == 3: # 위
                    dii, djj = i + di[d], j + dj[d]
                    if 0 <= dii < N and 0 <= djj < N:
                        sand = arr[dii][djj]
                        asand = arr[dii][djj]
                        arr[dii][djj] = 0
                        i, j = dii, djj

                    if sand > 0:
                        # 2%
                        if 0 <= dii < N and 0 <= djj - 2 < N:
                            arr[dii][djj - 2] += int((sand * 0.02) // 1)
                        else:
                            result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        if 0 <= dii < N and 0 <= djj + 2 < N:
                            arr[dii][djj + 2] += int((sand * 0.02) // 1)
                        else:
                            result += int((sand * 0.02) // 1)
                        asand -= int((sand * 0.02) // 1)

                        # 7%
                        if 0 <= dii < N and 0 <= djj - 1 < N:
                            arr[dii][djj - 1] += int((sand * 0.07) // 1)
                        else:
                            result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        if 0 <= dii < N and 0 <= djj + 1 < N:
                            arr[dii][djj + 1] += int((sand * 0.07) // 1)
                        else:
                            result += int((sand * 0.07) // 1)
                        asand -= int((sand * 0.07) // 1)

                        # 10%
                        if 0 <= dii - 1 < N and 0 <= djj - 1 < N:
                            arr[dii - 1][djj - 1] += int((sand * 0.1) // 1)
                        else:
                            result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        if 0 <= dii - 1 < N and 0 <= djj + 1 < N:
                            arr[dii - 1][djj + 1] += int((sand * 0.1) // 1)
                        else:
                            result += int((sand * 0.1) // 1)
                        asand -= int((sand * 0.1) // 1)

                        # 1%
                        if 0 <= dii + 1 < N and 0 <= djj - 1 < N:
                            arr[dii + 1][djj - 1] += int((sand * 0.01) // 1)
                        else:
                            result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        if 0 <= dii + 1 < N and 0 <= djj + 1 < N:
                            arr[dii + 1][djj + 1] += int((sand * 0.01) // 1)
                        else:
                            result += int((sand * 0.01) // 1)
                        asand -= int((sand * 0.01) // 1)

                        # 5%
                        if 0 <= dii + 2 * di[d] < N and 0 <= djj + 2 * dj[d] < N:
                            arr[dii + 2 * di[d]][djj + 2 * dj[d]] += int((sand * 0.05) // 1)
                        else:
                            result += int((sand * 0.05) // 1)
                        asand -= int((sand * 0.05) // 1)

                        # a%
                        if 0 <= dii + di[d] < N and 0 <= djj + dj[d] < N:
                            arr[dii + di[d]][djj + dj[d]] += asand
                        else:
                            result += asand
        if (i, j) == (0, 0): break
    turn += 2
print(result)