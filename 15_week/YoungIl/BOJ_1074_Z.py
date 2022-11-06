def search(n, ty, tx, count):
    if n == 0:                      # 가장 작은 2x2 사각형일 때
        return count
    temp = 0                        # 몇 사분면에 있는지 확인하는 숫자
    if ty >= 2**(n-1):              # 아래 사분면이면
        temp += 2                   # 위에 2개 사분면을 더해줘야 한다.
        ty -= 2**(n-1)              # 이후에 탐색해야 할 범위는 윗 부분을 잘라낸만큼 축소시킨다.
    if tx >= 2**(n-1):              # 오른쪽 사분면이라면
        temp += 1                   # 왼쪽에 1개 사분면을 더해줘야 한다.
        tx -= 2 ** (n-1)            # 이후에 탐색해야 할 범위는 왼쪽 부분을 잘라낸만큼 축소시킨다.
    count += temp * (2**(n-1)) * (2**(n-1))     # 잘라낸 사분면의 갯수에 잘라낸 사분면의 크기를 곱해서 더해준다.
    return search(n-1, ty, tx, count)           # 잘려진 부분에서 다시 탐색


N, target_y, target_x = map(int, input().split())
ans = search(N, target_y, target_x, 0)
print(ans)

