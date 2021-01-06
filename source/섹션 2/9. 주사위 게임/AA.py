"""
1에서부터 6까지의 눈을 가진 3개의 주사위를 던진다.
1. 같은 눈이 3개가 나오면 10000원 + 같은 눈 * 1000원
2 . 같은 눈이 2개만 나오는 경우 1000원 * 같은 눈 * 100원
3. 모두 다른 눈이 나오는 경우는 그 중 가장 큰 눈 * 100원의 상금을 받습니다.
N 명이 주사우 게임에 참여했을 때 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을
작성하세요.
"""
import sys
# sys.stdin = open('섹션 2\\9. 주사위 게임\\input.txt')

N = int(input())
result = 0
for i in range(N):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b and b == c:
        total = 10000 + a * 1000

    elif a == b or a == c:
        total = 1000 + (a * 100)

    elif b == c:
        total = 1000 + (b * 100)

    else:
        total = c * 100

    if total > result:
        result = total

print(result)