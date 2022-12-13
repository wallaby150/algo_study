import sys
sys.stdin = open("input.txt")

def q_out(commands:list, first_num:int):
    gostack = [-1 for _ in range(10001)]
    top = 0
    gostack[top] = first_num
    for command in commands:
        if 'NUM' in command:
            number = command.replace('NUM ','')
            top += 1
            gostack[top] = int(number)
        elif command == 'POP':
            # 수 부족하면 에러
            if top == -1: return 'ERROR'
            top -= 1
        elif command == 'INV':
            gostack[top] = -gostack[top]
        elif command == 'DUP':
            top_num = gostack[top]
            top += 1
            gostack[top] = top_num
        # 여기서부터 top = 0이면 전부 에러
        # 나눗셈 관련 부호 처리에 유의(문제에서 제시된 부분에 집중)
        # 두번째 수 (연산자) 첫번째 수 임에 주의
        # 연산 결과 절대값이 10 ** 9 넘어가도 에러(이상 x 초과 o)
        elif command == 'SWP':
            if top == 0: return 'ERROR'
            else: gostack[top], gostack[top-1] = gostack[top-1], gostack[top]
        elif command == 'ADD':
            if top == 0 or abs(gostack[top] + gostack[top-1]) > 10**9: return 'ERROR'
            else:
                result = gostack[top] + gostack[top-1]
                top -= 1
                gostack[top] = result
        elif command == 'SUB':
            if top == 0 or abs(gostack[top-1] - gostack[top]) > 10**9: return 'ERROR'
            else:
                result = gostack[top-1] - gostack[top]
                top -= 1
                gostack[top] = result
        elif command == 'MUL':
            if top == 0 or abs(gostack[top] * gostack[top-1]) > 10**9: return 'ERROR'
            else:
                result = gostack[top] * gostack[top - 1]
                top -= 1
                gostack[top] = result
        elif command == 'DIV':
            if top == 0 or gostack[top] == 0 or abs(gostack[top-1] // gostack[top]) > 10**9: return 'ERROR'
            else:
                if gostack[top-1] * gostack[top] < 0 :
                    result = abs(gostack[top-1]) // abs(gostack[top]) * -1
                else:
                    result = abs(gostack[top-1]) // abs(gostack[top])
                top -= 1
                gostack[top] = result
        elif command == 'MOD':
            if top == 0 or gostack[top] == 0 or (abs(gostack[top - 1]) % abs(gostack[top])) > 10**9: return 'ERROR'
            else:
                if gostack[top-1] <0:
                    result = abs(gostack[top-1]) % abs(gostack[top]) * -1
                else:
                    result = abs(gostack[top - 1]) % abs(gostack[top])
                top -= 1
                gostack[top] = result
    # 스택에 하나 이상의 수가 남아있다면 ERROR
    if top == 0: return gostack[top]
    else: return 'ERROR'

query = 0
this_query = []
this_num = []

while query != 'QUIT':
    query = input()
    if query != '':
        command, *num = query.split()
        if command != 'END' and not command.lstrip('-').isdecimal():
            this_query.append(query)
        # 음수도 포함해야하는데 is~ 들은 음수 문자열을 숫자로 인식하지 않아 임시방편 처리
        elif command.lstrip('-').isdecimal():
            this_num.append(int(query))
    else:
        # print(this_query)
        # print(this_num)
        # 숫자 배열의 첫번째 수는 전체 개수를 의미하므로 첫번째부터
        for num in this_num[1:]:
            print(q_out(this_query,num))
        print('')
        # 사용이 끝난 쿼리워 숫자를 비워줍니다.
        this_query = []
        this_num = []
