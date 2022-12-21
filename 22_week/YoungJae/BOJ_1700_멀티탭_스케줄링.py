n, k = map(int, input().split())
# 딕셔너리 dt
dt = {i:[] for i in range(1, k + 1)}
ls = list(map(int, input().split()))
# 멀티탭에 처음 다 꽂고 난 후 사용순서를 dt에 저장
for i in range(n, k): dt[ls[i]].append(i)
# 인덱싱 오류 막기 위해 k+1을 전부 추가
for i in range(1, k + 1): dt[i].append(k+1)
# 멀티탭 mt, 결과 rst
mt = []
rst = 0
for i in range(k):
    # 이미 꽂혀있으면 패스
    if ls[i] in mt: continue
    # 남는 멀티탭이 있으면 꽂기
    if len(mt) < n: mt.append(ls[i]); continue
    # 어느 플러그를 뽑아야 할지
    # 최대 순서 mx, 해당 순서의 물품이 어느 플러그에 꽂혀있는지 mi
    mx = mi = 0
    for j in range(n):
        k = 0
        while 1:
            # 해당 물품의 다음 순서 확인
            d = dt[mt[j]][k]
            # 이미 사용한 순서이면 다음으로 넘어감
            if d <= i: k += 1; continue
            # 기존 최대 순서보다 크면 mn, mi 저장
            if mx < d: mn = d; mi = j
            break
    # 플러그를 빼는 것이므로 + 1
    rst += 1
    # 플러그 교체
    mt[mi] = ls[i]
print(rst)