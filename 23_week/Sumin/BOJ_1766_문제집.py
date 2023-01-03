import sys
import heapq
# sys.stdin = open('input.txt')
input = sys.stdin.readline

# BOJ 1766 문제집

# 변수 선언 및 저장 =============================================================

N,M = map(int,input().split())    # N : 문제 수 / M : 선행 문제 정보 수
problem_prev = {}                 # 선행 문제. 3 1 로 입력 -> {1: [3]}
problem_next = {}                 # 후속 문제. 3 1 로 입력 -> {3: [1]}
for n in range(1,N+1):
    problem_prev[n] = []
    problem_next[n] = []
for m in range(M):
    prev, next = map(int,input().split())
    problem_prev[next].append(prev)
    problem_next[prev].append(next)

# 우선순위 큐를 이용한 push & pop ================================================
# 우선순위 큐는 기본적으로 작은 순서대로 뱉는 성질을 이용 (정렬)

solved = [0 for _ in range(N+1)] # 해당 문제가 풀렸는지 체크. 1번 인덱스부터 사용
solve_hq = []   # 우선순위 큐
result = []     # 결과를 저장할 리스트

# 선행 문제가 없어 바로 풀 수 있는 문제들을 최초에 우선순위 큐에 넣고
for n in range(1,N+1):
    if problem_prev[n] == []:
        heapq.heappush(solve_hq,n)

def other_pb_check(n): # 재귀 함수
    global solve_hq
    for npb in problem_next[n]:
        if all(solved[pb] == 1 for pb in problem_prev[npb]):
            heapq.heappush(solve_hq,npb)    # 선행해야하는 모든 문제가 풀린 상태라면 우선순위 큐에 추가
            other_pb_check(npb)             # 해당 문제가 풀림으로서 풀려지는 다른 문제들이 있는지 확인합니다.

while solve_hq:
    n = heapq.heappop(solve_hq) # 우선순위 큐에서 현재 풀 수 있는 문제 중 숫자가 작은 순서대로 꺼냅니다.
    solved[n] = 1               # 해당 문제를 이 시점에서 풀었다고 체크
    result.append(n)            # 나오는 순서대로 result에 저장합니다. 이는 그대로 정답이 됩니다.
    other_pb_check(n)           # 해당 문제가 풀림으로서 풀려지는 다른 문제들이 있는지 확인합니다.

# 정답 출력
for r in result:
    print(r,end=' ')




