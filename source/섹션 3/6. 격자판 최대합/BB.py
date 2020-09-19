'''
격자판 최대합
5*5 격자판에 아래와 같이 숫자가 적혀있습니다.
10 18 10 12 15
12 39 30 28 11
11 25 50 53 15
19 27 29 37 27
19 18 30 13 19

N * N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.

입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

출력설명
최대합을 출력합니다.

입력예제
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
10 27 29 37 27
19 13 30 13 19

출력예제
155
'''

import sys
sys.stdin = open('C:/Users/user/project_code/source/섹션 3/6. 격자판 최대합/in5.txt', 'r')

N = int(input())

list_N = [list(map(int, input().split())) for _ in range(N)] # 2차원 리스트 입력 방법. [[0] * 3 for _ in range(3)]

raw_max = col_max = 0
for col in range(N):
    raw_sum = 0
    for raw in range(N):
        raw_sum += list_N[col][raw]

    if raw_sum > raw_max:
        raw_max = raw_sum

for raw in range(N):
    col_sum = 0
    for col in range(N):
        col_sum += list_N[raw][col]

    if col_sum > col_max:
        col_max = col_sum

dia_sum_1 = dia_sum_2 = dia_max = 0
for i in range(N):
    dia_sum_1 += list_N[i][i]
    dia_sum_2 += list_N[i][N-i-1]

if dia_sum_1 > dia_sum_2:
    dia_max = dia_sum_1

else:
    dia_max = dia_sum_2

result = 0
if raw_max > col_max:
    result = raw_max
else:
    result = col_max

if result > dia_max:
    print(result)
else:
    print(dia_max)