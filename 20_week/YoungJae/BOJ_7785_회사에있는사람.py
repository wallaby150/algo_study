# 출력횟수 c
c = 0
g = int(input())
# 풀이
# y²-x² = (y+x)(y-x) = ji = g
# y-x = i, y+x = g//i
# y = (g/i+i)/2, x = (g/i-i)/2

# j > i이고 i가 클수록 j=y+x가 작아지므로 √g부터 1까지 i를 찾음
# 1. i, j는 자연수의 합과 차의 곱이므로 정수여야 함 => g % i == 0 (i는 for문으로 제어)
# 2. x, y는 몸무게이므로 0보다 커야 함 : x > 0 (y>x이므로 y는 확인하지 않아도 됨)
# 3. x, y는 자연수여야 함 : 2y % 2 = 0 (둘 중 하나가 자연수면 나머지 하나는 자연스럽게 자연수)
for i in range(int(g**.5), 0, -1):
    if g % i == 0 and ((g // i) - i) // 2 > 0 and (g // i + i) % 2 == 0: print((g // i + i) // 2); c += 1
# 출력한 적이 없으면 -1 출력
if c == 0: print(-1)