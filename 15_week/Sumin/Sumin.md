# BOJ_1516_게임 개발

https://www.acmicpc.net/problem/1516

![](README_img/Pasted%20image%2020221108211122.png)

**접근 방법**

- 위상 정렬을 사용
  - 위상 정렬이란? 방향성이 있고 사이클이 없는 graph에서 선행하는 일을 끝내고 다음 일을 처리해 순서를 도출하는 방법
  - 여러 개의 답이 있을 수 있으며, stack을 사용하는 방법과 queue를 사용하는 방법이 있다.
  - 해당 문제에서는 queue에 진입차수가 0인 노드를 넣은 후, 해당 노드를 꺼낼 때마다 그 노드가 진입하는 다른 노드의 차수를 감소시켜 다음으로 진입차수가 0이 된 것들을 차례로 넣어주는 식으로 진행
  - 이 경우 큐에서 빠져나온 순서 == 위상 정렬의 해답
- 각 노드가 수행되기까지의 최소 시간을 구하기 위해 진입 차수가 0인 노드를 빼낼 때마다 선행하는 노드들의 수행 시간 중 최대 시간을 기존 값에 더해 기록(메모이제이션)

```python
from collections import deque

N = int(input())
structs = [tuple(map(int,input().split())) for _ in range(N)]

# 진입 차수 기록 배열. 1번 노드부터 사용(0번 인덱스 사용 X)
# index 1에는 노드 1로 들어오는 진입 차수의 개수가 기록된다.
# 해당 배열 진입차수가 0이 되는 노드들을 큐에 넣어줄 예정
input_char = [0 for _ in range(N+1)]

# 자신이 어느 노드에 진입하고 있는지를 기록하는 배열. 1번 노드부터 사용(0번 인덱스 사용 X)
# index 1에 [2,3,4] 가 기록된 경우 1번 노드는 2,3,4번 노드로 진입한다
# 진입차수가 0이 되어 큐에서 빠져나온 노드는 해당 배열을 확인해서
# 진입중인 노드로의 진입을 해제한다 (이 경우 2,3,4번 진입차수가 1 감소)
child_nodes = [[] for _ in range(N+1)]

# 각 노드의 일(건물 완성) 까지 걸리는 최단 시간을 기록할 배열
# 1번 노드부터 사용(0번 인덱스 사용 X)
# 초기값으로 각 건물을 짓는데 드는 비용을 기록해준 후,
# 선행되어 지어져야할 건물들의 소비 시간을 더해 기록해줄 배열이기도 함(메모이제이션)
result = [0]


for idx in range(0,N):
    struct = structs[idx]
    # 초기값으로 각 건물을 지을때 드는 시간을 추가
    result.append(struct[0])
    # 1번 노드부터 마지막의 -1을 제외하고, 각 노드의 진입차수와 어디로 진입하는지 기록
    for s in range(1,len(struct)-1):
        input_char[idx+1] += 1
        child_nodes[struct[s]].append(idx+1)
        
q = deque([])
# 현재 진입차수가 0인 노드를 q에 추가
for ic in range(1, len(input_char)):
    if input_char[ic] == 0:
        q.append(ic)

# 여기서부터 위상정렬
# 진입차수가 0이 되어 빠져나온 노드들이 순차적으로 line에 들어간다
# line에 들어간 값 순서 == 건물이 순차적으로 지어져야할 여러 순서 중 하나
# 해당 문제에서는 visited 대용으로 사용했습니다.
line = []

while q:
    # 진입 차수가 0인 노드를 꺼내 line에 기록 후
    v = q.popleft()
    line.append(v)
    # 해당 노드가 진입 중인 연결을 모두 해제 == 진입 중인 곳의 진입차수 -1
    for idx in child_nodes[v]:
        input_char[idx] -= 1
        # 만약 이 작업으로 해당 노드의 진입차수가 0이 된 곳이 있으며
        # 아직 q에서 빠져나온 적 없는(처리되지 않은) 노드라면
        # 선행되어야 할 건물들 중 최대인 시간을 찾아 기존 값에 더하기(메모이제이션)
        # 이 값을 result에 기록 후 해당 노드를 큐에 넣습니다
        if input_char[idx] == 0 and idx not in line:
            struct = structs[idx-1]
            max_time = 0
            for s in range(1, len(struct) - 1):
                sdx = struct[s]
                if max_time < result[sdx]:
                    max_time = result[sdx]
            q.append(idx)
            result[idx] += max_time

# 만약 모든 노드 방문 전에 q가 빌 경우, 사이클이 존재해 위상 정렬이 실패한 것
# 하지만 문제에서 모든 건물을 짓는 것이 가능한 경우만 주어진다고 했으므로 따로 처리 X

# result에 기록된 값을 차례로 출력
for r in range(1,len(result)):
    print(result[r])
```



**느낀 점**

- 위상정렬에 대해 언급으로만 들었는데 직접 풀어보며 익힐 수 있었다.

- 문제의 유형을 사전에 알지 못하더라도 이런 풀이를 생각해낼 수 있도록 연습해야겠다.