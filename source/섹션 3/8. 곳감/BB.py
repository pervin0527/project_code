import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/8. 곳감/input.txt', 'r')

N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

# 행을 기준으로 왼쪽 또는 오른쪽으로 회전.
# 명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 회전.

for _ in range(M):
    a, b, c = map(int, input().split())

    if b == 0: # 왼쪽으로
        for i in range(c):
            list_N[a-1].append(list_N[a-1].pop(0))

    else: # 오른쪽으로
        for i in range(c):
            list_N[a-1].insert(0, list_N[a-1].pop())

# print(list_N)

# 모레시계 모양으로 합산.
p1 = 0
p2 = N
total = 0

for i in range(N):
    for j in range(p1, p2):
        total += list_N[i][j]

    if i < N //2:
        p1 += 1
        p2 -= 1

    else:
        p1 -= 1
        p2 += 1

print(total)