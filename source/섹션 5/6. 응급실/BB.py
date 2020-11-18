import sys
from collections import deque

sys.stdin = open("source\\섹션 5\\6. 응급실\\input.txt", "r")
N, M = map(int, input().split()) # M은 제일 처음 환자를 0번째로 간주하여 표현한 것.
list_N = [(idx, value) for idx, value in enumerate (list(map(int, input().split())))] # 접수한 순서대로 위험도
# print(N, M, list_N) # 5 2 [(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)]

dq = deque(list_N)
# print(dq)
cnt = 0

while True:
    cur = dq.popleft()

    if any(cur[1] < x[1] for x in dq): # 현재 진료 받을 사람의 위험도 보다 높은 사람이 한 명이라도 있다면 True
        dq.append(cur)

    else:
        cnt+=1 # 없으면 현재 진료 받을 사람의 위험도가 가장 높다는 뜻이므로 cnt 증가.

        if cur[0] == M:
            break

print(cnt)