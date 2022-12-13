import sys
sys.stdin = open('input.txt')

log_num = int(input())
company = {}
for i in range(log_num):
    person, inout = input().split()
    if inout == 'enter':
        company[person] = 1
    else:
        if person in company:
            company[person] = 0
result = []
for p in company:
    if company[p] == 1: result.append(p)

result.sort(reverse=True)
for p in result:
    print(p)