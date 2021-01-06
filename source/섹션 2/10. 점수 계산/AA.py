"""
여러 개의 OX문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주려 한다.
1번 문제가 맞는 경우에는 1점으로 계산
앞의 문제에 대해서 답을 틀리고 이후 답이 맞는 처음 문제는 1점으로 계산
연속으로 답이 맞는 경우에서 두번째 문제는 2점 세번째 문제는 3점으로
k번째 문제는 k점으로 계산한다. 틀린 문제는 0점으로 계산.
"""
import sys
# sys.stdin = open('섹션 2\\10. 점수 계산\\input.txt')

N = int(input())
list_N = list(map(int, input().split()))
check_list = [0] * N

tmp = 0
for i in range(N):
    if list_N[i] == 1:
        tmp += 1
        check_list[i] = tmp

    else:
        tmp = 0

result = sum(check_list)
print(result)