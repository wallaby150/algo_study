holes, usages = map(int, input().split())       # 멀티탭 구멍의 개수, 전기 용품의 총 사용횟수
use_orders = list(map(int, input().split()))    # 사용할 순서
plugs = [0] * holes                             # 현재 멀티탭 상태
count = 0                                       # 교체 횟수


for now_order in range(usages):                 # 사용 순서를 쭉 훑어본다.
    now_tool = use_orders[now_order]            # 지금 사용할 도구

    # 이미 꽂혀있는 놈이면 넘어간다.
    if now_tool in plugs:
        continue

    # 아직 빈 구멍이 있으면
    if 0 in plugs:
        # 해당 구멍의 인덱스에 지금 순서의 전기 용품의 번호를 넣는다.
        idx = plugs.index(0)
        plugs[idx] = now_tool

    # 꽉 찼다면
    else:
        count += 1          # 교체 횟수 +1
        later_usage = 0     # 가장 늦게 사용될 애의 번호
        later_idx = 0       # 가장 늦게 사용될 애의 인덱스

        for hole in range(holes):   # 콘센트의 구멍의 인덱스를 돌아보며
            plug = plugs[hole]      # 해당 인덱스에 꽂혀있는 애

            # 다시 안 쓸 녀석 찾으면 걔를 빼고 써야 되는 친구를 넣는다.
            if plug not in use_orders[now_order:]:
                plugs[hole] = now_tool
                break

            # 아니면 제일 늦게 사용되는 애를 찾는다.
            elif use_orders[now_order:].index(plug) > later_idx:
                later_usage = plug
                later_idx = use_orders[now_order:].index(plug)

        else:
            # 제일 늦게 사용되는 애를 빼고 지금 써야 할 애를 꽂는다.
            plugs[plugs.index(later_usage)] = now_tool

print(count)
