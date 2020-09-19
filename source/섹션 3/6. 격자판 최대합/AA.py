import sys
# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/6. 격자판 최대합/input.txt', 'r')

N = int(input())

list_N = [list(map(int, input().split())) for _ in range(N)] # 2차원 리스트 입력 방법. [[0] * 3 for _ in range(3)]

largest = -2147000000

for i in range(N):
    sum1 = sum2 = 0

    for j in range(N):
        sum1 += list_N[i][j]
        sum2 += list_N[j][i]

    if sum1 > largest:
        largest = sum1

    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(N):
    sum1 += list_N[i][i]
    sum2 += list_N[i][N-i-1]

if sum1 > largest:
    largest = sum1

if sum2 > largest:
    largest = sum2

print(largest)