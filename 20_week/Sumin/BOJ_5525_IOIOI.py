import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())    # PN 패턴의 N
M = int(input())    # S의 길이
S = input()         # 주어진 문자열
# S 안에 PN 패턴이 몇 군데 포함되어있는가?

# IOI 패턴이 N번 등장하면 result 값을 추가
result = 0
cursor = 0
nn = N

while cursor < M - 1 :
    if S[cursor: cursor+3] == 'IOI':
        nn -= 1
        cursor += 2
        # N번 등장했다면 result 값 추가 후 nn 체크 변수를 1 증가
        # 이후 같은 IOI 패턴이 한 번 더 나온다면 동일한 패턴이 또 있는 것이므로
        if nn == 0:
            result += 1
            nn += 1
    else:
        # IOI 패턴이 더 이상 나오지 않는다면 nn 초기화 및 커서 1칸씩 이동
        cursor += 1
        nn = N

print(result)
















# s = 0
# nn = N
# isPN = False
# while s < M-2 :
#     if S[s] == 'I':
#         if S[s+1] == 'O' and S[s+2] == 'I':
#             if isPN:
#                 nn -= 1
#                 if nn == 0:
#                     result += 1
#                     nn = N
#                     isPN = False
#                     s -= 2 * (N-2)
#                 else: s += 2
#             else:
#                 isPN = True
#                 nn -= 1
#                 s += 2
#                 if nn == 0:
#                     result += 1
#                     nn = N
#                     isPN = False
#         else:
#             isPN = False
#             nn = N
#             s += 1
#     else:
#         isPN = False
#         nn = N
#         s += 1
#
# print(result)