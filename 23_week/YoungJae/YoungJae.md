# BOJ_1234 토끼의 이동

## 문제 주소
https://www.acmicpc.net/problem/3101

- 문제
1부터 N2까지 수가 지그재그 대각선 순서로 N*N 행렬에 채워져 있다. 아래 그림은 N=6일 때, 행렬의 모습이다.

1	2	6	7	15	16
3	5	8	14	17	26
4	9	13	18	25	27
10	12	19	24	28	33
11	20	23	29	32	34
21	22	30	31	35	36
토끼는 지금 1이 있는 칸에 있다. 토끼는 인접한 칸으로 점프할 수 있다. (위, 아래, 오른쪽, 왼쪽)

토끼가 점프한 방법이 주어졌을 때, 토끼가 방문한 칸에 있는 수의 합을 구하는 프로그램을 작성하시오. 같은 칸을 여러 번 방문할 경우에도, 방문할 때 마다 더해야 한다. 토끼가 행렬을 벗어나는 경우는 없다.

- 입력
첫째 줄에 N, K가 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ K ≤ 300,000) N은 행렬의 크기, K는 토끼가 점프한 횟수이다.

둘째 줄에는 'U','D','L','R'로 이루어진 문자열이 주어진다. 이 문자열의 길이는 K이며, 토끼가 점프한 방향이다.

- 출력
첫째 줄에, 방문한 칸의 수의 합을 출력한다. 이 값은 32비트 정수를 넘을 수도 있다.

## 문제 접근 방법
N ≤ 100,000 이므로 N×N의 이중 리스트를 만들면 10^10으로 리스트 한 칸 당 4비트로 잡으면 5,000MB로 메모리 제한인 128MB를 한참 넘게 된다. 이를 해결하기 위해 각 칸에 배정하는 것이 아닌 행 열 위치를 바탕으로 한 계산으로 해결한다.

이를 해결하기 위해선 좌표를 가로 세로로 보는게 아닌 대각선으로 바라봐야 하기 때문에 새로운 좌표계를 잡았다.
s : / 방향을 잡기 위한 좌표 (x+y)
c : 행렬 좌하단을 0으로 잡고, 우상단으로 갈수록 1이 늘어가게 잡는다.

이후 s를 기준으로 짝수이면 좌하단에서 우상단으로 1씩 늘어나게, 홀수이면 우상단에서 좌하단으로 1씩 늘어나게 계산되도록 한다.

### 코드
```python
# 방향에 따른 좌표 이동
dr = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
n, k = map(int, input().split())
ls = list(input())
# 각 대각줄의 길이 ln, 각 대각줄의 최대값 sm
ln = list(range(n)) + list(range(n-2, -1, -1))
sm = [1]
for i in range(1, len(ln)): sm.append(sm[i-1] + ln[i] + 1)

# 시작점 (0,0), cnt 1
y = x = 0
cnt = 1
# 이동 명령
for d in ls:
    # 이동에 따라 x,y 좌표 이동
    y += dr[d][0]; x += dr[d][1]
    # s, c 좌표 계산
    s = y + x
    # 0 ~ n-1까지는 c는 x좌표랑 동일
    # 그보다 커지면 커짐에 따라 좌우로 1칸씩은 행렬 밖으로 벗어남
    # c 좌표는 좌하단부터만 계산하기 때문에 좌측 1칸씩만 빼는 것이므로 x - (s - (n - 1))로 계산
    if s < n: c = x
    else: c = x + n - 1 - s
    # s가 홀수면 좌하단으로 갈수록 커지므로 최대값 - c
    # 짝수면 우상단으로 갈수록 커지므로 최소값(sm - ln)에 c 좌표 추가
    if s % 2: ss = sm[s] - c
    else: ss = sm[s] - ln[s] + c
    cnt += ss
print(cnt)
```

### 시간복잡도
O(N + K) = O(max(N, K))

### 공간복잡도
O(N + N) = O(N)

# 느낀 점
수를 넣는 방식이 이질적이라 계산하는 것에 시간을 많이 쓴 문제였다.