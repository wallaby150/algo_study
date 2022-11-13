import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int,input().split()))
# X 중복 제거 후 정렬
srt = sorted(set(x))
# 인덱스 부여해 딕셔너리로 저장
dic = {srt[i]:i for i in range(len(srt))}
# 딕셔너리로 인덱스 불러냄
for a in x: print(dic[a], end=' ')