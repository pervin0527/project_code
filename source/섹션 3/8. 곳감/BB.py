import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/8. 곳감/input.txt', 'r')

N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for _ in range(M):
    a, b, c = map(int, input().split())
    # print(a, b, c)

    if b == 0:
        for i in range(c):
            tmp = list_N[a-1].pop(0)
            # print(tmp, list_N)
            list_N[a-1].append(tmp)
            # print(list_N)

    else:
        for i in range(c):
            tmp = list_N[a-1].pop()
            # print(tmp, list_N)
            list_N[a-1].insert(0, tmp)
# print(list_N)
start = 0
end = N - 1
bp = N // 2
result = 0
for i in range(N):
    for j in range(start, end + 1):
        result += list_N[i][j]

    if i < bp:
        start += 1
        end -= 1

    else:
        start -= 1
        end += 1

print(result)