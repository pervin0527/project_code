import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/1. 회문 문자열 검사/input.txt')

N = int(input())

for i in range(N):
    boca = input()
    boca = boca.upper()
    # print(boca)

    for j in range(len(boca) // 2):
        if boca[j] != boca[-1-j]:
            print("#%d NO" % (i+1))
            break

    else:
        print("#%d YES" % (i+1))