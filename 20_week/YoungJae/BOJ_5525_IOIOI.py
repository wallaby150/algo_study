n = int(input())
m = int(input())
s = input()
# 개수 cnt, 체크위치 i, 반복횟수 k
cnt = 0
i = 0
k = 0
# 'IOI'가 최소 1번은 나와야 하기 때문에 m-2까지 확인
while i < m-2:
    # 해당 위치에 'IOI'가 있으면 k+1하고 P_N 만족하는지 확인
    # P_N을 만족하면 cnt를 늘리고 연속되어 있을 수 있으니 k는 1만 줄임 ex) IOIOIOI는 P2가 2개 있다.
    # P_N을 만족하지 않으면 2칸 뒤 확인
    # 'IOI'가 없으면 1칸 뒤 확인, k 초기화
    if s[i:i+3] == 'IOI':
        k += 1
        if k == n: cnt += 1; k -= 1
        i += 2
    else: i += 1; k = 0
print(cnt)