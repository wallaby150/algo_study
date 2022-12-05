def search(paint):
    visited = list([0] * N for _ in range(N))
    count = 0
    queue = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                count += 1
                queue.append((y, x))
            while queue:
                now_y, now_x = queue.pop(0)
                for direction in range(4):
                    ny, nx = now_y+dy[direction], now_x+dx[direction]
                    if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                        if paint[y][x] == paint[ny][nx]:
                            visited[ny][nx] = 1
                            queue.append((ny, nx))
    return count


N = int(input())
original_paint = []     # 원래 그림
changed_paint = []      # 적록색약의 그림

for _ in range(N):
    temp = input()
    original_paint.append(temp)
    changed_paint.append(temp.replace('G', 'R'))    # 적록색약의 그림은 아예 초록을 빨강으로 변경해서 저장

print(search(original_paint), search(changed_paint))    # 기존 그림과 변경한 그림을 각각 search함수에 넣어준다.