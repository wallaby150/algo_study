### \# BOJ_5430_AC

```python
from collections import deque

for _ in range(int(input())):
    func_list = input().replace("RR", "")       # 두 번 뒤집는 경우는 배제시켜주자.
    n = int(input())
    txt = input()
    if n == 0:
        array = deque()
    else:
        array = deque(txt[1:-1].split(","))     # 입력받은 텍스트를 데크 형태로 변환시켜준다.
    R_switch = False

    for func in func_list:
        if func == "R":
            R_switch = not R_switch
        elif func == "D":
            if len(array) == 0:     # 빈 데크에서 꺼낼 요소가 없으니 에러
                print("error")
                break
            else:
                if R_switch:        # 거꾸로 된 상황이라면
                    array.pop()     # 오른쪽 요소를 꺼내고
                else:
                    array.popleft()     # 그게 아니면 왼쪽에서 꺼낸다.
    else:
        if R_switch:                # 거꾸로 스위치 켜져있으면 뒤집기
            array.reverse()
        print('[' + ','.join(array) + ']')
```

- 처음에 'R'을 입력받을 때마다 reverse()를 사용했는데, 시간이 너무 오래 걸렸다.
- 기본적으로 list나 deque를 그대로 출력하면 항목 간의 공백이 존재하기 때문에 join을 사용해야 했다.
- pop(0)도 list형태로는 시간복잡도가 O(n)이기 때문에, 이를 해결하기 위해서 deque의 popleft()를 사용한다.