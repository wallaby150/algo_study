[백준 5525_IOIOI](https://www.acmicpc.net/problem/5525)



## 조건
- N+1개의 I와 N개의 O로 이루어져 있으면서, I와 O가 교대로 나오는 문자열을 Pn 이라고 한다.
- P1 = IOI, P2 = IOIOI
- I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 Pn이 몇 군데 포함되어 있는지 구하는 프로그램 작성
- 1<=N<=1,000,000
- 2N+1 <= M <= 1,000,000
- ooioioioi 인경우 ioi가 3번나온다.



## 접근 방법
- n에 따른 target 길이에 따라 슬라이싱 범위를 정해준다.
- 또한 n에 따른 target 문자열을 반복문을 통해 생성해준다.

위처럼 target 문자열을 생성해주니 50점 받음 

```python
import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
  
N = int(input())  
M = int(input())  
S = input()  
  
target = ''  
for j in range(N*2+1):  
    if j %2 ==0:  
        target += 'I'  
    else:  
        target += 'O'  
  
  
cnt = 0  
for i in range(M-(N*2+1)):  
    if S[i:i+(N*2+1)] == target:  
        cnt+=1  
  
print(cnt)
```




- I와 O를 따로 구하는 것이 아닌 'IO'가 N만큼 나온 후 뒤에 I가 붙어있다면 +1 해주면 된다.

위처럼 슬라이싱을 이용해주어서 반복문이 하나 줄었지만 그래도 50점.. 

```PYTHON
import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
  
N = int(input())  
M = int(input())  
S = input()  
  
cnt = 0  
for i in range(M-1):  
    if S[i:i+N*2] == 'IO'*N and S[i+N*2] == 'I':  
        cnt += 1  
print(cnt)
```



- 시간을 조금더 줄여보기 위해 인덱스를 뛰어 넘으며 검사해주면 될 것 같다.
- IOI를 1 패턴으로 보고 PATTERN 수가 M만큼 나온다면  CNT+1
- 또한 PATTERN -= 1을 해주며 연속된 Pn을 찾아준다.
- 다음 I의 인덱스는 최소 시작 +2
- IOI가 아니라면 pattern 수 초기화 및 i+=1


```PYTHON
import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
  
N = int(input())  
M = int(input())  
S = input()  
  
  
cnt = 0  
  
i = 0  
pattern = 0  
while i < M-2:  
    if S[i:i+3] == 'IOI':  
        pattern +=1  
        if pattern == N:  
            cnt += 1  
            pattern -= 1  
        i += 2  
    else:  
        pattern = 0  
        i += 1  
print(cnt)
```