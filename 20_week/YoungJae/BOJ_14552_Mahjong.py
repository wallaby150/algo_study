# 패 체크 함수, h는 머리, b는 몸통, i는 체크한 위치
def chkpae(pp, h=0, b=0, i=1):
    # 머리 1개, 몸통 4개가 모두 만들어졌으면 True 반환
    if h == 1 and b == 4: return True
    # 패 복사해서 가져오기
    pae = pp[:]
    # 낮은 숫자부터 패 확인
    while i < 10:
        # 패를 가지고 있다면
        if pae[i] > 0:
            # 3장 이상이고 몸통이 4 미만이면 몸통으로 넣고 되는지 확인
            if pae[i] >= 3 and b < 4:
                pae[i] -= 3; rst = chkpae(pae, h, b+1, i)
                # 된다면 더 할 것 없이 바로 종료
                if rst: return True
                # 안되면 원상복구
                pae[i] += 3
            # 2장 이상이고 머리가 없으면 머리로 넣고 확인
            if pae[i] >= 2 and not h:
                pae[i] -= 2; rst = chkpae(pae, h+1, b, i)
                if rst: return True
                pae[i] += 2
            # 연속된 세 숫자가 있으면 몸통에 넣고 확인
            if i < 8 and pae[i+1] and pae[i+2]:
                pae[i] -= 1; pae[i+1] -= 1; pae[i+2] -= 1
                rst = chkpae(pae, h, b+1, i)
                if rst: return True
            # 모두 안되면 남는 패가 있으므로 불가능 선언
            return False
        else: i += 1


ls = list(map(int, input().split()))
# 패 세팅 (i번째 패가 몇 개 있는지로 변경)
pae = [0]*10
for i in ls: pae[i] += 1
rst = []
# 대기패 확인, 1부터 한 패씩 패에 넣어봄
for i in range(1, 10):
    # 패는 4장까지이므로 4장이면 넘어감
    if pae[i] == 4: continue
    pp = pae[:]
    # 패에 추가
    pp[i] += 1
    # 치또이(머리 7개) 확인
    p7 = 0
    for j in range(1, 10):
        if not pp[j] % 2: p7 += pp[j] // 2
    if p7 == 7: rst.append(i)
    # 아니면 완성 되는지 확인
    elif chkpae(pp): rst.append(i)
if rst: print(*rst)
else: print(-1)