# BOJ_17144 미세먼지 안녕!

## 문제 주소
https://www.acmicpc.net/problem/17144

- 문제
미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 $A_{r,c}$이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다.
(r, c)에 남은 미세먼지의 양은 $A_{r,c}$ - ($A_{r,c/5}$)×(확산된 방향의 개수) 이다.
공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
다음은 확산의 예시이다.

왼쪽과 오른쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.

인접한 네 방향으로 모두 확산이 일어난다.

공기청정기가 있는 칸으로는 확산이 일어나지 않는다.

공기청정기의 바람은 다음과 같은 방향으로 순환한다.

방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

- 입력
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.

둘째 줄부터 R개의 줄에 $A_{r,c}$ (-1 ≤ $A_{r,c}$ ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 $A_{r,c}$가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

- 출력
첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.

## 문제 접근 방법
처음에는 구현/시뮬레이션 문제인 줄 알고 단순히 미세먼지 확산과 공기청정기 활동을 구현해보았지만 시간초과로 PyPy3에서만 성공이 뜨는 코드가 나왔다. 이를 Python3에서도 시간초과가 나지 않게 하기 위해 아래와 같이 개선해나갔다.
- 공기청정기 위치 저장 : 기존에는 두 위치 모두 x,y좌표를 저장하는 리스트로 저장했지만, 어차피 공기청정기의 두 위치는 위아래로 이어져있고 x좌표는 0으로 고정이기 때문에 아래 공기청정기의 y좌표 위치만 잡고, 검색을 위한 for문도 2중에서 1중으로 변경하였다.
- np의 활용 : 기존에는 tt초에 일어난 일을 모두 np에 저장 후 deepcopy를 통해 전달하였지만, 이게 너무 비효율적이라 생각해 np는 먼지 확산할 때 확산양만 저장한 후 하나씩 mp에 더하는 방식으로 진행하였다.
- 델타탐색 : 먼지 확산과 공기 순환 모두 델타 탐색을 썼지만 조건문에서 이득이 되지도 않고 하단 순환에서는 불필요한 연산을 계속 하게 되는 것 같아 델타탐색을 포기하고 if문 4개를 통해 표현하게 되었다.
- 먼지 확산 기준 : 기존에는 먼지가 있으면 무조건 확산작업을 하였지만, A//5는 A>=5일 때 확산되는 것이므로 기준을 5 이상으로 잡아 불필요한 탐색횟수를 줄였다.
- 함수 활용 : 사실 이 부분은 실제로 시간단축이 되는지는 모르겠지만 조금 더 해당 코드가 어떤 코드인지 확인하기 편하고 많은 사람들이 사용하는 방법이기 때문에 이를 활용해보았다.

### 코드
```python
# PyPy3
import sys
input = sys.stdin.readline
from copy import deepcopy

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
r, c, t = map(int, input().split())
mp = []
ac = []
# map 불러오기, 공기청정기 위치 저장
for i in range(r):
    mp.append(list(map(int, input().split())))
    for j in range(c):
        if mp[i][j] == -1: ac.append((i,j))

for tt in range(t):
    # 먼지 확산양 저장을 위해 np 생성
    np = [[0] * c for _ in range(r)]
    # 공기청정기 위치 저장
    for a, b in ac: np[a][b] = -1
    # 먼지 확산
    # 0 이상이면 확산 진행
    for y in range(r):
        for x in range(c):
            if mp[y][x] > 0:
                # a 저장 후 np에 추가
                a = mp[y][x]
                np[y][x] += a
                # 델타탐색으로 맵 내부이고 공기청정기가 아니면 확산
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < r and 0 <= nx < c and mp[ny][nx] >= 0:
                        np[ny][nx] += a//5
                        np[y][x] -= a//5
    # 공기청정기 활동
    # 상단 순환
    y, x = ac[0]
    # y가 최상단이면 순환되지 않음
    if y > 0:
        yy, xx = y, x
        y -= 1
        # 사방으로 while문을 통해 끝가지 회전
        for d in range(4):
            while 1:
                ny, nx = y + dy[d], x + dx[d]
                if ny < 0 or ny > yy or nx < 0 or nx >= c: break
                # 공기청정기를 만나면 순환이 끝난거기 때문에 0으로 바꾸고 break
                if np[ny][nx] == -1: np[y][x] = 0; break
                np[y][x] = np[ny][nx]
                y, x = ny, nx
    # 하단 순환
    y, x = ac[1]
    # y가 최하단이면 순환되지 않음
    if y < r-1:
        yy, xx = y, x
        y += 1
        for d in range(4):
            while 1:
                ny, nx = y + dy[(2-d)%4], x + dx[(2-d)%4]
                if ny < yy or ny >= r or nx < 0 or nx >= c: break
                if np[ny][nx] == -1: np[y][x] = 0; break
                np[y][x] = np[ny][nx]
                y, x = ny, nx
    # 회전한 내용 저장
    mp = deepcopy(np)
print(sum(sum(mp, []))+2)
```
```python
# python3
import sys
input = sys.stdin.readline

# 미세먼지 확산
def dust():
    # 이동되는 먼지 기록용 np
    np = [[0] * c for _ in range(r)]
    # 미세먼지 양이 5 이상이 아니면 확산되지 않음
    for y in range(r):
        for x in range(c):
            if mp[y][x] >= 5:
                a = mp[y][x] // 5
                # 확산 횟수 저장용 dc
                dc = 0
                # 상하좌우에 확산
                if y > 0 and mp[y-1][x] >= 0: np[y-1][x] += a; ac += 1
                if y < r-1 and mp[y+1][x] >= 0: np[y+1][x] += a; ac += 1
                if x > 0 and mp[y][x-1] >= 0: np[y][x-1] += a; ac += 1
                if x < c-1 and mp[y][x+1] >= 0: np[y][x+1] += a; ac += 1
                # 확산된만큼 제거
                mp[y][x] -= dc * a
    # np 값을 기존 map에 저장
    for i in range(r):
        for j in range(c):
            mp[i][j] += np[i][j]
# 공기청정기 회전
def spin():
    # 상단 회전
    for y in range(ac-3, -1, -1): mp[y+1][0] = mp[y][0]
    for x in range(c-1): mp[0][x] = mp[0][x+1]
    for y in range(ac-1): mp[y][c-1] = mp[y+1][c-1]
    for x in range(c-1, 0, -1): mp[ac-1][x] = mp[ac-1][x-1]
    # 하단 회전
    for y in range(ac+1, r-1): mp[y][0] = mp[y+1][0]
    for x in range(c-1): mp[r-1][x] = mp[r-1][x+1]
    for y in range(r-1, ac, -1): mp[y][c-1] = mp[y-1][c-1]
    for x in range(c-1, 0, -1): mp[ac][x] = mp[ac][x-1]
    # 공기청정기 우측은 0
    mp[ac-1][1] = mp[ac][1] = 0

r, c, t = map(int, input().split())
mp = []
# map 추가, 공기청정기 위치 ac에 저장
for i in range(r):
    mp.append(list(map(int, input().split())))
    if mp[i][0] == -1: ac = i
# t초동안 반복
for _ in range(t):
    dust()
    spin()
# 공기청정기 구간이 2이기 때문에 2를 더해놓고 합산
rst = 2
for x in range(r): rst += sum(mp[x])
print(rst)
```

### 시간복잡도
O(R) + O(T*(4RC+RC+2R+2C)) + O(R) = O(TRC)

### 공간복잡도
O(NM + NM) = O(NM)

# 느낀 점
평소 크게 생각하지 않는 부분에서 시간 소요가 생각보다 많이 된다는 것을 느꼈고 조금 더 간결하고 최적화된 코드를 작성하는 것의 중요함을 느꼈다.