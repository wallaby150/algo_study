from heapq import *

def solution(n, roads, sources, destination):
    answer = []
    # rd로 road 정보 재구조화
    rd = [[] for _ in range(n+1)]
    for i, j in roads: rd[i].append(j); rd[j].append(i)
    # 최소거리 d
    # 나올 수 있는 최댓값이 n이기 때문에 n+1로 설정
    d = [n+1]*(n+1)
    # 부대 위치를 0으로 설정
    d[destination] = 0
    q = [(destination, 0)]
    # dijkstra 알고리즘
    # 도착점에서 각 지점의 최소거리를 구함
    while q:
        m, c = heappop(q)
        # 갈 수 있는 거리 중 최소거리 갱신 가능하면 갱신 후 heap에 추가
        for a in rd[m]:
            if d[a] > c + 1: d[a] = c + 1; heappush(q, (a, c + 1))
    # 각 부대원 위치마다 최소거리 저장
    for s in sources:
        if d[s] == n+1: answer.append(-1)
        else: answer.append(d[s])
    return answer