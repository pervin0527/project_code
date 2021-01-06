# 자연수 p를 자연수 q로 나누었을때 나머지가 0이면 q는 p의 약수.
# N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성.

import sys
# sys.stdin = open('섹션 2\\1. k번째 약수\\input.txt')
N, K = map(int, input().split())
# print(N, K)

for x in range(1, N+1):
    if N % x == 0:
        K -= 1

    if K == 0:
        print(x)
        break

else:
    print(-1)