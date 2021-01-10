"""
유람선이 침몰하고 있습니다.
유람선에는 N명의 승객이 타고 있는데, 구명보트는 2명 이하로만 탈 수 있습니다.
보트 한 개에 탈 수 있는 총 무게가 M 이하로 제한되어 있습니다.
N명의 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를
출력하는 프로그램을 작성하세요.
"""
import sys
# sys.stdin = open('섹션 4/8. 침몰하는 타이타닉/input.txt')

N, M = map(int, input().split())
weight = list(map(int, input().split()))
# print(N, M, weight)

weight.sort(reverse=True)

cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break

    if weight[0] + weight[-1] <= M:
        cnt += 1
        weight.pop(0)
        weight.pop()

    else:
        cnt += 1
        weight.pop(0)

print(cnt)