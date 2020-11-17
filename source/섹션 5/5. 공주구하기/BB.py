import sys
from collections import deque

sys.stdin = open("source\\섹션 5\\5. 공주구하기\\input.txt", 'r')
N, K = map(int, input().split())
# print(N, K)

dq = list(range(1, N+1))
dq = deque(dq)

while dq:
    for _ in range(K-1):
        cur = dq.popleft()
        dq.append(cur)

    dq.popleft()

    if len(dq) == 1:
        break

print(dq[0])