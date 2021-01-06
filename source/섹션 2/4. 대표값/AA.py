"""
N명의 학생 성적이 주어집니다.
N명의 학생들의 평균(소수점 첫째자리 반올림)을 구하고, N명의 학생 중
평균에 가장 가까운 학생은 몇번째 학생인지 출력하는 프로그램을 작성하세요.
답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요.
답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 합니다.
"""

import sys
# sys.stdin = open('섹션 2\\4. 대표값\\input.txt')
N = int(input())
list_N = list(map(int, input().split()))

avg = int(sum(list_N) / len(list_N) + 0.5)
# print(avg)

best = 2147000000

for idx, x in enumerate(list_N):
    tmp = abs(avg - x)

    if tmp < best:
        best = tmp
        score = x
        number = idx + 1

    elif tmp == best:
        if x > score:
            score = x
            number = idx + 1 

print(avg, number)