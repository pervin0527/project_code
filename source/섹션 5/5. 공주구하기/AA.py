import sys
from collections import deque
# sys.stdin = open('섹션 5/5. 공주구하기/input.txt')

n, k = map(int, input().split())
a = list(x for x in range(1, n + 1))
dq = deque(a)

while dq:
    for _ in range(k-1):
        tmp = dq.popleft()
        dq.append(tmp)

    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()