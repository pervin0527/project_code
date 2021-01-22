import sys
# sys.stdin = open('섹션 5/9. 아나그램(구글)/input.txt')

a = input()
b = input()

a_dict = {}

for x in a:
    if x not in a_dict:
        a_dict[x] = 1

    else:
        a_dict[x] += 1

for x in b:
    if x in a_dict:
        a_dict[x] -= 1

for key, value in a_dict.items():
    if value != 0:
        print("NO")
        break

else:
    print("YES")