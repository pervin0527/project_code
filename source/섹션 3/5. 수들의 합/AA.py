"""
N개의 수로 된 수열 A[1], A[2], ... A[N]이 있다.
i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하세요.
"""
import sys
sys.stdin = open('섹션 3/5. 수들의 합/input.txt')

N, M = map(int, input().split())
a = list(map(int, input().split()))

# print(N, M)
# print(a)

lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < M:
        if rt < N: # n값 보다 작을때까지만 수열의 합 수행
            tot += a[rt]
            rt += 1

        else: #rt가 n과 같거나 n보다 커질 경우
            break

    elif tot == M:
        cnt += 1
        tot -= a[lt]
        lt += 1

    else:
        tot -= a[lt]
        lt += 1

print(cnt)
    