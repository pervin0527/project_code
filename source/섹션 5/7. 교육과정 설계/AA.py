import sys
from collections import deque
# sys.stdin = open('섹션 5/7. 교육과정 설계/input.txt')

f = input()
n = int(input()) # n개의 수업 설계

for i in range(n):
    a = input()
    dq = deque(f)

    for x in a:
        if x in dq:
            tmp = dq.popleft()

            if tmp != x:
                print("#%d NO" % (i + 1))
                break

    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))

        else:
            print("#%d NO" % (i + 1))