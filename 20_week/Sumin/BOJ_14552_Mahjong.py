import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 현재 덱 받아오기
deck = sorted(list(map(int,input().split())))

# 결과값 저장할 리스트
result = []

# head 1 , body 4 혹은 head 7 일때 결과를 저장
head, body = 0,0

# 1~9에 대한 딕셔너리 만들어서 개별 값 저장
one_nine = {}
for i in range(1,10):
    one_nine[i] = 0
for i in range(0,13):
    one_nine[deck[i]] += 1

# 1~9 중 하나의 패를 넣어 14개 패가 완성되는지 확인
# r = 넣을 패 번호
for r in range(1,10):
    # 하나의 패는 4개 이하여야 하므로 넣을 수 있을 때만 넣는다
    if one_nine[r] < 4:
        one_nine[r] += 1

        # 머리 7개가 완성되는지 확인한다.
        for i in range(1,10):
            # 이 때, 11 11 은 개별 머리로 칠 수 없으므로 무조건 각 패는 2개씩 있어야 함
            if one_nine[i] == 2:
                one_nine[i] -= 2
                head += 1
        # 머리 7개라면 패가 완성되므로 결과값에 저장 후 연산 초기화(one_nine 딕셔너리 정상화)
        if head == 7:
            result.append(r)
            head = 0
            one_nine = {}
            for i in range(1, 10):
                one_nine[i] = 0
            for i in range(0, 13):
                one_nine[deck[i]] += 1
            one_nine[r] += 1
        # 머리7개 패가 완성되지 않는다면,
        else:
            # 앞선 연산 초기화 (one_nine 딕셔너리 정상화)
            head = 0
            one_nine = {}
            for i in range(1, 10):
                one_nine[i] = 0
            for i in range(0, 13):
                one_nine[deck[i]] += 1
            one_nine[r] += 1

            # 머리 하나를 선정한 후 나머지가 전부 몸통을 이루는지 확인
            # 머리부터 선정
            for i in range(1,10):
                if one_nine[i] >= 2:
                    one_nine[i] -= 2
                    head += 1
                    # 남은 패가 연속패, 같은패 등으로 전부 차감되는지 확인한다.
                    for j in range(1,10):
                        while one_nine[j] >= 3:
                            one_nine[j] -= 3
                            body += 1
                        while j < 8 and one_nine[j] >= 1 and one_nine[j+1] >= 1 and one_nine[j+2] >=1 :
                            one_nine[j] -= 1
                            one_nine[j+1] -= 1
                            one_nine[j+2] -= 1
                            body += 1
                    # 머리 하나와 몸 4개가 성공적으로 만들어졌으며, 기존 결과에 없는 값이라면 추가
                    if head == 1 and body == 4 and r not in result:
                        result.append(r)
                    # 연산 초기화 (one_nine 딕셔너리 정상화)
                    head,body = 0, 0
                    one_nine = {}
                    for i in range(1, 10):
                        one_nine[i] = 0
                    for i in range(0, 13):
                        one_nine[deck[i]] += 1
                    one_nine[r] += 1
        # 연산 초기화 (one_nine 딕셔너리 정상화)
        one_nine[r] -= 1

# 가능한 결과값이 없을 때 -1 출력
if result == []: result.append(-1)
# 결과값 순차 출력
for r in result: print(r, end=" ")