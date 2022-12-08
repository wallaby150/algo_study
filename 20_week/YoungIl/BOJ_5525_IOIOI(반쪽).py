N = int(input())
s_length = int(input())
S = input()

text = "IO" * N + "I"

count = 0
for i in range(s_length-len(text)+1):
    if S[i] == "O":
        pass
    elif S[i:i+len(text)] == text:
        count += 1

print(count)