import sys
input = sys.stdin.readline

# 방향 dr, dc
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = map(int, input().split())
# 파이어볼 저장용 리스트 fb
fb = []
# 나중 계산을 편리하게 하기 위해 r, c를 1씩 배서 fb에 추가
for _ in range(m):
    r, c, *o = map(int, input().split())
    fb.append([r-1, c-1] + o)
# k번 명령 반복
for _ in range(k):
    # 이동 후 위치 저장용 rc
    rc = {}
    # 파이어볼 이동 후 rc에 저장
    for r, c, w, s, d in fb:
        r = (r + dr[d] * s) % n; c = (c + dc[d] * s) % n
        if rc.get((r, c), 0): rc[r,c].append([w, s, d])
        else: rc[(r, c)] = [[w, s, d]]
    # 새 결과 집어넣기 위해 fb를 비움
    fb = []
    # 같은 위치에 있는 파이어볼 처리
    for r, c in rc:
        # 같은 곳에 있으면 병합/분할작업
        if len(rc[(r, c)]) > 1:
            [sw, ss, od, ed] = [0]*4
            for w, s, d in rc[(r, c)]:
                sw += w
                ss += s
                # 방향 보고 od, ed 체크
                if d % 2: od += 1
                else: ed += 1
            sw //= 5; ss //= len(rc[(r, c)])
            # 짝수 홀수 둘 다 나왔으면 1 아니면 0
            dd = 1 if od and ed else 0
            # 질량이 남아있으면 fb에 4등분한 파이어볼 추가
            if sw:
                for k in range(4): fb.append([r, c, sw, ss, k*2+dd])
        # 아니면 그냥 파이어볼 추가
        else: fb.append([r, c] + rc[(r, c)][0])
rst = 0
for f in fb: rst += f[2]
print(rst)