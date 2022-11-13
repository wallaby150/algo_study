# 최댓값 1,000,001 저장
mx = 1000001
# 리스트 생성
nm = [1] * mx
# 에라토스테네스의 채
# 3부터 홀수마다 소수인지 확인 후 리스트에 저장
# 소수이면 소수의 배수는 전부 0으로 변경
# 0~2, 짝수는 어차피 확인하지 않을 것이기 때문에 패스
for i in range(3, 1001, 2):
    if nm[i]:
        for j in range(i * 2, mx, i): nm[j] = 0
# 골든바흐의 추측
while 1:
    n = int(input())
    # n = 0이면 중지
    if not n: break
    # 3 ~ n/2까지 홀수 중 i와 n-i가 모두 소수면 출력
    # 아직 해결되지 않은 추측이므로 반례는 발견되지 않았을 것이므로 else는 고려하지 않음
    for i in range(3, n//2+1, 2):
        if nm[i] and nm[n-i]: print(n, '=', i, '+', n-i); break