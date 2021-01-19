import sys
from collections import deque
# sys.stdin = open('섹션 5/6. 응급실/input.txt')

n, m = map(int, input().split())
a = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# print(n, m, a)

dq = deque(a)
cnt = 0

while True:
    tmp = dq.popleft()

    # any 함수는 인자로 받은 반복 가능한 자료형 중 단 하나로 참이 있으면 True
    # 모든 요소가 거짓인 경우에만 False
    if any(tmp[1] < x[1] for x in dq):
        dq.append(tmp)

    else:
        cnt += 1
        if tmp[0] == m:
            break

print(cnt)