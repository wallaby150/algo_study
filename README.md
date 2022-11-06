# \# Triple_A - Algorithm Study

> 코딩 테스트 준비를 위한 스터디입니다.

- 참고 사이트: [프로그래머스](https://programmers.co.kr/learn/challenges), [백준](https://www.acmicpc.net/)
- 언어: 파이썬



## \- PR 규칙 및 Commit Message 규칙

### PR 방법 : [깃허브 알고리즘 스터디용 (tistory.com)](https://codingpracticing.tistory.com/91) 참고



#### Pull Request

- [n주차] 이름

#### Commit Message

- [PROG-문제번호] 문제명 _ 프로그래머스
- [BOJ-문제번호] 문제명
- [SWEA-문제번호] 문제명



## \- 파일 및 폴더 구조

- n_week\이름\사이트\_문제번호_문제명.py

  ex) 15_week\YoungIl\BOJ_1074_Z.py

-> ! 11월 첫째 주 기준 15_week !



## `이름.md` Rule

- 각 폴더별 `이름.md` Rule은 다음을 참고한다
  - **문제 주소**, **문제 접근 방법** 를 작성한다.
  - **문제 접근 방법** 은 되도록이면 구체적으로 작성한다.

ex) YoungIl.md

~~~markdown
# 문제 주소
https://www.acmicpc.net/problem/1000

## 문제 접근 방법
인풋을 int형으로 변환하여 A, B 각각의 변수에 저장한 뒤 합쳤다. 

### 코드
```python
A, B = map(int, input().split())
print(A + B)
```
### 시간복잡도
O(1)

### 공간복잡도
O(1)

# 느낀 점
~~~