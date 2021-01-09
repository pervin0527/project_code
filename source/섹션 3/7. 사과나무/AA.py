"""
현수의 농장은 N * N 격자판으로 이루어져 있습니다.
각 격자안에는 한 그루의 사과 나무가 심어져 있고, N의 크기는 항상 홀수입니다.
사과를 수확할 때는 격자판 내에서 다이아몬드 모양 내에 있는 사과만 수확합니다.
"""
import sys
sys.stdin = open('섹션 3/7. 사과나무/input.txt')
N = int(input())
a = [list(map(int, input().split())) for i in range(N)]
# print(a)

cnt = 0
p1 = p2 = bp = int(N//2)

for i in range(N):
    for j in range(p1, p2 + 1):
        cnt += a[i][j]

    if i < bp:
        p1 -= 1
        p2 += 1

    else:
        p1 += 1
        p2 -= 1

print(cnt)