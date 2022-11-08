from collections import deque

N = int(input())
structs = [tuple(map(int,input().split())) for _ in range(N)]

input_char = [0 for _ in range(N+1)]
child_nodes = [[] for _ in range(N+1)]
result = [0]
for idx in range(0,N):
    struct = structs[idx]
    result.append(struct[0])
    for s in range(1,len(struct)-1):
        input_char[idx+1] += 1
        child_nodes[struct[s]].append(idx+1)
q = deque([])
for ic in range(1, len(input_char)):
    if input_char[ic] == 0:
        q.append(ic)

line = []

while q:
    v = q.popleft()
    line.append(v)
    for idx in child_nodes[v]:
        input_char[idx] -= 1
        if input_char[idx] == 0 and idx not in line:
            struct = structs[idx-1]
            max_time = 0
            for s in range(1, len(struct) - 1):
                sdx = struct[s]
                if max_time < result[sdx]:
                    max_time = result[sdx]
            q.append(idx)
            result[idx] += max_time

for r in range(1,len(result)):
    print(result[r])

