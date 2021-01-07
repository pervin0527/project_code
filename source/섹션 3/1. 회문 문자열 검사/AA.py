"""
N개의 문자열 데이터를 입력 받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우
YES를 출력하고 그렇지 않으면 NO를 출력하는 프로그램을 작성하세요.
단 검사 시 대소문자 구분은 하지 않습니다.
"""
import sys
# sys.stdin = open('섹션 3/1. 회문 문자열 검사/input.txt')

N = int(input())

for i in range(N):
    boca = str(input())
    boca = boca.lower()

    for j in range(int(len(boca)/2)):
        if boca[j] != boca[-j-1]:
            print("#%d NO" % (i + 1))
            break

    else:
        print("#%d YES" % (i + 1))