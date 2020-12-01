import sys

# sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\9. 아나그램(구글)\\input.txt", "r")

a = input()
b = input()
res1 = dict()
res2 = dict()

for s in a:
    res1[s] = res1.get(s, 0) + 1

for s in b:
    res2[s] = res2.get(s, 0) + 1

for i in res1.keys():
    if i in res2.keys():
        if res1[i] != res2[i]:
            print("NO")
            break

    else:
        print("NO")
        break

else:
    print("YES")