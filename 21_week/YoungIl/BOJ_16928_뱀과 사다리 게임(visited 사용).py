from collections import deque


def bfs():
    now_nums = deque([1])      # BFS 형식으로 탐색하기 위해서 현재 위치와 주사위를 굴린 횟수를 저장하는 리스트를 저장하는 이중 리스트(데크)를 만듭니다.
    visited[1] = True          # 첫 시작한 부분 방문 표시

    while now_nums:
        now_num = now_nums.popleft()

        for possible in range(now_num+1, now_num+7):
            if possible <= 100 and not visited[possible]:
                if possible in ladders_dict.keys():         # 사다리가 있는 칸이면
                    possible = ladders_dict[possible]
                elif possible in snakes_dict.keys():        # 뱀이 있는 칸이면
                    possible = snakes_dict[possible]

                if not visited[possible]:                   # 사다리/뱀을 타고도 안 가본 곳이면
                    now_nums.append(possible)               # 큐에 저장
                    visited[possible] = True                # 방문 표시
                    board[possible] = board[now_num] + 1    # 몇 번 굴렸는지 표시


ladders_n, snakes_n = map(int, input().split())         # 사다리와 뱀의 수를 각각 저장합니다.
ladders_dict = dict(map(int, input().split()) for _ in range(ladders_n))        # 사다리의 정보를 받아서 dict형태로 저장합니다.
snakes_dict = dict(map(int, input().split()) for _ in range(snakes_n))          # 뱀의 정보를 받아서 dict형태로 저장합니다.
visited = [False] * 101     # 해당 칸을 가봤는지 확인하는 리스트
board = [0] * 101           # 몇 번 굴려서 도착했는지

bfs()
print(board[100])

# 시간이 108ms -> 64ms로 줄었다.