import sys

sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\9. 아나그램(구글)\\input.txt", "r")

a = input()
b = input()
res1 = dict()
res2 = dict()

for s in a:
    if not s in res1:
        res1[s] = 1

    else:
        res1[s] += 1

for s in b:
    if not s in res2:
        res2[s] = 1

    else:
        res2[s] += 1

if res1 == res2:
    print("YES")

else:
    print("NO")