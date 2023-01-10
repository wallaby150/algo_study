txt = input()
target = input()
n = 0

while n != len(txt):
    n = len(txt)
    txt = txt.replace(target, "")

if txt:
    print(txt)
else:
    print("FRULA")