import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/9. 봉우리/input.txt', 'r')

N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]

# 격자의 가장자리는 0으로 초기화
list_N.insert(0, [0] * N)
list_N.append([0] * N)

for i in list_N:
    i.insert(0, 0)
    i.append(0)

# print(list_N)

# 자신의 상하좌우 숫자보다 큰 숫자는 봉우리.
cnt = 0
p1 = [-1, 0, 1, 0]
p2 = [0, 1, 0, -1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if all(list_N[i][j] > list_N[i+p1[k]][j+p2[k]] for k in range(4)):
            cnt += 1

print(cnt)