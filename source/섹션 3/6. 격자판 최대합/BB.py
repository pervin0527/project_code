import sys
sys.stdin = open('C:/Users/user/project_code/source/섹션 3/6. 격자판 최대합/input.txt', 'r')

N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]

# print(list_N)
# 각 행의 합, 각 열의 합, 두 대각선의 합 구하기

maximum = 0

for i in range(N):
    total_raw = total_col = 0

    for j in range(N):
        total_raw += list_N[i][j]
        total_col += list_N[j][i]

    if total_raw > maximum:
        maximum = total_raw

    if total_col > maximum:
        maximum = total_col


total_1 = total_2 = 0
for i in range(N):
    total_1 += list_N[i][i]
    total_2 += list_N[i][-1-i]

if total_1 > maximum:
    maximum = total_1

if total_2 > maximum:
    maximum = total_2

print(maximum)