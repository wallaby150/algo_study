import sys
sys.stdin=open('input.txt')

import sys
#input=sys.stdin.readline
#1202 보석 도둑
import heapq
#N=보석 개수, K=가방 개수 1 이상 300,000 이하
N,K=map(int,sys.stdin.readline().split())
#각 보석 무게 Mi, 가격 Vi 1,000,000 이하
hq=[]
for n in range(N):
    Mi,Vi=map(int,sys.stdin.readline().split())
    heapq.heappush(hq,[Mi,Vi])
#가방에 담을 수 있는 최대 무게 100,000,000 이하
Ci=[]
for k in range(K):
    Ci.append(int(sys.stdin.readline()))
Ci.sort()
result=0
jew=[]
#print(hq[0])
#print(hq)
for bag in Ci:
    while hq and bag>=hq[0][0]:
        heapq.heappush(jew,-heapq.heappop(hq)[1])
    if jew:
        result-=heapq.heappop(jew)
    elif not hq:
        break
print(result)
