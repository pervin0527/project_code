import sys
import heapq as hq

sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\10. 최소힙\\input.txt", "r")

a = []

while True:
    x = int(input())

    if x == -1:
        break

    if x == 0:
        if len(a) == 0:
            print(-1)

        else:
            print(-hq.heappop(a))

    else:
        hq.heappush(a, -x)