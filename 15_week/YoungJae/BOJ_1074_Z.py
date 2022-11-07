
# Z자로 돌아다닐 때 2행은 1행에 +2를 한 것과 같고,
# 2열을 1열에 +1을 한 것과 같음
n, r, c = map(int, input().split())
# 크기 지정
x1, y1, x2, y2 = 0, 0, 2**n-1, 2**n-1
cnt = 0
# 반복
while n > 0:
    # 결과 4배시킴
    cnt *= 4
    # y / x의 절반 위치 찾아줌
    mdx, mdy = (x1+x2)//2, (y1+y2)//2
    # c가 x 중앙보다 크면 cnt에 +1
    if c > mdx: cnt += 1; x1 = mdx
    else: x2 = mdx
    # r이 y 중앙보다 크면 cnt에 +2
    if r > mdy: cnt += 2; y1 = mdy
    else: y2 = mdy
    n -= 1
print(cnt)