"""
N개의 문자열 데이터를 입력 받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우이면
YES를 출력하고 그렇지 않으면 NO를 출력하는 프로그램을 작성한다.
단 검사할 때 대소문자를 구분하지 않습니다.

입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다.
각 단어의 길이는 100을 넘지 않는다.

출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

입력예제
5
level
moon
abcba
soon
gooG

출력예제
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
"""

import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/1. 회문 문자열 검사/input.txt')

N = int(input())

idx = 1
for i in range(N):
    boca = str(input()) # 문자열은 그대로 input 받아도 전체 다 입력 됨
    boca = boca.lower() # 대문자를 소문자로 바꿔주는 역할

    list_s = []
    for s in boca:
        list_s.append(s)
    list_s.reverse()

    reversed_boca = ''
    for s in list_s:
        reversed_boca += s
    
    # print(reversed_boca, boca)

    if str(reversed_boca) == str(boca):
        print('#%d YES' %idx)

    else:
        print('#%d NO' %idx)

    idx += 1

    

    

