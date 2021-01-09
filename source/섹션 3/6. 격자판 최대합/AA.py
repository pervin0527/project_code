"""
5 * 5 격자판에 숫자가 적혀있습니다.
N * N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중
가장 큰 합을 출력합니다.
"""
import sys
# sys.stdin = open('섹션 3/6. 격자판 최대합/input.txt')

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
maximum = -2147000000

for i in range(N):
    row_sum, col_sum = 0, 0
    for j in range(N):
        row_sum += a[i][j]
        col_sum += a[j][i]

    if row_sum > col_sum:
        tmp = row_sum

    else:
        tmp = col_sum

    if tmp > maximum:
        maximum = tmp

# print(maximum)

left_dig, right_dig = 0, 0
for i in range(N):
    left_dig += a[i][i]
    right_dig += a[i][N-i-1]

if left_dig > right_dig:
    tmp = left_dig

else:
    tmp = right_dig

if tmp > maximum:
    maximum = tmp

print(maximum)