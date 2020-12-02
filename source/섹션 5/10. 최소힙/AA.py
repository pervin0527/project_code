import sys
import heapq as hq

sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\10. 최소힙\\input.txt", "r")

a = []

while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) # root 노드 값을 출력

    else:
        hq.heappush(a, n) # a라는 리스트에 n이라는 값을 넣음