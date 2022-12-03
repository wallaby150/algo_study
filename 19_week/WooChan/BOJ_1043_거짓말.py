# https://www.acmicpc.net/problem/1043
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

# 진실을 알고 있는 사람
know = list(map(int, sys.stdin.readline().split()))
if len(know) > 1:
    know = set(know[1:])    # 사람 수 제외
else:
    know = set()

# 각 파티별 참여자
party_people = []
for _ in range(M):
    party_people.append(list(map(int, sys.stdin.readline().split())))

# 각 파티별 참여자 수 제외
for i in range(len(party_people)):
    if len(party_people[i]) > 1:
        party_people[i] = set(party_people[i][1:])
    else:
        party_people[i] = set(party_people[i])

count = 1   # 진실을 알고 있는 사람의 수에 변동이 있는지 체크할 변수
while count != 0:   # 변동이 있으면 반복
    count = 0   # 일단 변동 없음
    i = 0       # 각 파티를 순회하기 위한 idx값
    while i < len(party_people):    # 각 파티 순회
        if know & party_people[i]:      # i번째 파티 참여자 중에 진실을 아는 사람이 있으면
            know = know | party_people[i]       # 그 파티의 참여자들도 진실을 알게 된다
            party_people.remove(party_people[i])        # 해당 파티에서는 과장할 수 없으므로 제외
            count += 1      # 진실을 아는 사람의 수에 변동이 있음을 체크
        else:
            i += 1

# 남은 파티는 과장할 수 있는 파티
answer = len(party_people)
print(answer)