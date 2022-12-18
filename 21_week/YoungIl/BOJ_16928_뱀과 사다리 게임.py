from collections import deque


def bfs():
    now_nums = deque([[1, 0]])      # BFS 형식으로 탐색하기 위해서 현재 위치와 주사위를 굴린 횟수를 저장하는 리스트를 저장하는 이중 리스트(데크)를 만듭니다.
    while now_nums:
        now_num, roll_count = now_nums.popleft()
        trigger = False             # 6부터 1까지 내려오면서 사다리나 뱀이 없다면 가장 큰 숫자를 선택하기 위한 트리거
        for possible in range(now_num + 6, now_num, -1):
            if possible >= 100:
                return roll_count + 1       # 주사위를 굴려서 100을 넘어가면 도착한 것이므로 return
            if possible in ladders_dict.keys():         # 사다리가 있는 칸이면
                now_nums.append([ladders_dict[possible], roll_count + 1])       # 사다리를 탄 값을 저장
            elif possible in snakes_dict.keys():        # 뱀이 있는 칸이면
                now_nums.append([snakes_dict[possible], roll_count + 1])        # 뱀을 탄 값을 저장
            elif not trigger:       # 트리거가 아직 작동 전이면(가장 큰 수를 선택하지 않았다면)
                now_nums.append([possible, roll_count + 1])     # 지금 수가 가장 큰 수
                trigger = True      # 그 밑에 숫자는 따로 queue에 저장하지 않기 위해서 트리거 작동


ladders_n, snakes_n = map(int, input().split())         # 사다리와 뱀의 수를 각각 저장합니다.
ladders_dict = dict(map(int, input().split()) for _ in range(ladders_n))        # 사다리의 정보를 받아서 dict형태로 저장합니다.
snakes_dict = dict(map(int, input().split()) for _ in range(snakes_n))          # 뱀의 정보를 받아서 dict형태로 저장합니다.

print(bfs())