# 버스 이동 계산
def bus(ls):
    # 버스 이동 거리 rst, 현재 버스 탑승 인원 t
    rst = 0; t = 0
    for l, m in ls:
        while 1:
            # 버스에 인원이 없으면 학교를 갔다 온거기 때문에 새 곳으로 이동
            # 왔다갔다니 * 2
            if not t: rst += l * 2
            # 현재 지역 인원이 다 타도 정원초과가 안나면 태우고 다음 지역 이동
            if k >= m + t: t += m; break
            # 정원초과 나면 전부 태우고 남은 인원만 m에 남겨두고
            # t는 학교를 갔다올거기 때문에 0으로 처리
            m += t - k; t = 0
    return rst

n, k, s = map(int, input().split())
rp = {}; rm = {}
for _ in range(n):
    i, j = map(int, input().split())
    # 학교보다 멀리 있으면 rp에 가까이 있으면 rm에 추가
    if i > s: rp[i - s] = j
    else: rm[s - i] = j
# 각각을 정렬
rp = sorted(rp.items(), reverse=True)
rm = sorted(rm.items(), reverse=True)
# +지역 갔다가 m지역 갔다가 학교 가는 일은 최소거리가 아니기 때문에
# 각각의 경우를 나눠서 합산
print(bus(rm) + bus(rp))