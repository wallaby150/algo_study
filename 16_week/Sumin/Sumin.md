# BOJ_23293_아주 서바이벌

**접근 방법**

- 구현
- 문제가 알쏭달쏭해서 이해해서 잘 풀어야 하는 문제!!
- 각 조건에 따라 로그를 기록하고, 요구사항에 맞춰서 출력
- 차단은 공격 치트 쓴 사람에 한해서. 로그 기록 자체는 전부 해야 합니다.

```python
T, N = map(int,input().split())
logs = [()]
now_player = {}

for i in range(1, N+1):
    now_player[i] = [1, []]  # 현재 장소, 파밍한 아이템

for i in range(1, T+1):
    logs.append(tuple(map(lambda x: int(x) if x.isdecimal() else x, input().split())))

bad_logs = []

bad_players = []
for i in range(1, T+1):
    idx, player, commend, *cnums = logs[i]
    if commend == 'M': # Move
        now_player[player][0] = cnums[0]
    if commend == 'F': # Farming
        if now_player[player][0] != cnums[0]:
            if bad_logs == [] or bad_logs[-1][0] != idx:
                bad_logs.append((idx,player,commend,cnums))

        now_player[player][1].append(cnums[0])
    if commend == 'C': # Crafting
        for cnum in cnums:
            if cnum not in now_player[player][1]:
                if bad_logs == [] or bad_logs[-1][0] != idx:
                    bad_logs.append((idx, player, commend, cnums))
            else:
                now_player[player][1].remove(cnum)
    if commend == 'A': # Attack
        target = cnums[0]
        if now_player[player][0] != now_player[target][0]:
            if bad_logs == [] or bad_logs[-1][0] != idx:
                bad_logs.append((idx, player, commend, cnums))
            if player not in bad_players:
                bad_players.append(player)

bl_num = len(bad_logs)
print(bl_num)
if bl_num > 0:
    for i in range(bl_num):
        print(bad_logs[i][0], end=' ')
    print()
bad_players.sort()
bp_num = len(bad_players)
if bp_num == 0:
    print(bp_num, end=' ')
else:
    print(bp_num)
    for i in range(bp_num):
        print(bad_players[i],end=' ')
```

**느낀 점**

- 문제를 잘 파악하고 예외 처리를 빠짐없이 진행하자