import sys
from collections import deque

sys.stdin = open("source\\섹션 5\\7. 교육과정 설계\\input.txt", "r")

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i+1))
                break

    else:
        if len(dq) == 0:
            print("#%d YES" % (i+1))
        else:
            print("#%d NO" % (i+1))