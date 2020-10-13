import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/7. 사과나무/input.txt', 'r')
N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]

# print(list_N)

p1 = p2 = bp = N // 2
total = 0

for i in range(N):
    for j in range(p1, p2 + 1):
        total += list_N[i][j]

    if i < bp:
        p1 -= 1
        p2 += 1

    else:
        p1 += 1
        p2 -= 1

print(total)