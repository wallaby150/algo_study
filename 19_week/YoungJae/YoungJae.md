# BOJ_1202 보석 도둑

## 문제 주소
https://www.acmicpc.net/problem/1202

- 문제

세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

- 입력

첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.

- 출력

첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

## 문제 접근 방법
한 가방에 하나만 넣을 수 있으니 가장 작은 가방부터 넣을 수 있는 최대 값어치의 보석을 넣자고 생각했다.

큰 가방부터 생각한다면 작은 가방에도 넣을 수 있는 보석을 넣어 공간을 낭비할 수 있으니 작은 가방부터 고려하게 된다.

보석의 경우 우선 가방에 넣을 수 있는지 확인해야 하기 때문에 무게순으로 정렬한 후, 넣을 수 있는 보석들 중에서는 최대가치를 가져가야 하기 때문에 가격순으로 정렬하게 된다.

이러한 과정을 조금 더 편하게 하기 위해 우선순위 큐를 두 번 사용한다.

### 코드
```python
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
# 보석 저장
# 무게 순으로 heappush
jew = []
for _ in range(n): heapq.heappush(jew, list(map(int, input().split())))
# 가방 저장 후 무게 오름차순 정렬
bag = []
for _ in range(k): bag.append(int(input()))
bag.sort()
# 결과
rst = 0
# 가방에 담을 수 있는 보석의 가치 저장용 tmp
tmp = []
# 작은 가방부터 채우기
for b in bag:
    # 넣을 수 있는 보석들을 tmp에 가격순으로 넣기
    while jew and b >= jew[0][0]: heapq.heappush(tmp, -heapq.heappop(jew)[1])
    # 그 중 가장 값어치 있는 보석을 넣음
    if tmp: rst -= heapq.heappop(tmp)
    # 보석이 더 없으면 종료
    elif not jew: break
print(rst)
```

### 시간복잡도
O(NK)

### 공간복잡도
O(max(2N, K))

# 느낀 점
우선순위 큐를 2번 쓰는 것이 조금 신박했던 문제였다.