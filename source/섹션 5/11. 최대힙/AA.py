import sys
import heapq as hq

# sys.stdin = open('섹션 5/11. 최대힙/input.txt')
a = []

while True:
    x = int(input())

    if x == -1:
        break

    if x == 0:
        if len(a) == 0:
            print('-1')

        else:
            print(-(hq.heappop(a)))

    else:
        hq.heappush(a, -x)