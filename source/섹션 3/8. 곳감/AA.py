"""
현수의 마당은 N * N 격자판으로 이루어져 있으며,
각 격자단위로 말리는 감의 수를 정합니다. 그런데 해의 위치에 따라
특정 위치의 감은 잘 마르지 않습니다. 그래서 현수는 격장의 행을 기준으로
왼쪽 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 2 0 3 이면 2번째 행을 왼쪽으로 3만큼 이동 시킵니다.
12 39 30 23 11 -> 23 11 12 39 30
M개의 회전명령을 실행하고 난 후 모래시계 영역에 감이 총 몇개 있는지 출력하세요.
"""
import sys
sys.stdin = open('섹션 3/8. 곳감/input.txt')

N = int(input())
a = [list(map(int, input().split())) for i in range(N)]

M = int(input())
for i in range(M):
    # 행, 방향, x만큼
    q, w, e = map(int, input().split())

    if w == 0:
        for j in range(e):
            a[q-1].append(a[q-1].pop(0))

    else:
        for j in range(e):
            a[q-1].insert(0, a[q-1].pop())

print(a)

p1 = 0
p2 = N
res = 0
for i in range(N):
    for j in range(p1, p2):
        res += a[i][j]

    if i < (N // 2):
        p1 += 1
        p2 -= 1

    else:
        p1 -= 1
        p2 += 1

print(res)