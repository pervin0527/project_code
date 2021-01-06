"""
두 개의 정N면체와 정M면체 주사위를 던져서 나올 수 있는 눈의 합 중
가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
"""
import sys
# sys.stdin = open("섹션 2\\5. 정다면체\\input.txt")

N, M = map(int, input().split())
check_list = [0] * (N+M+1)

for i in range(1, N):
    for j in range(1, M):
        tmp = i + j
        check_list[tmp] += 1

maximum = -2147000000
for i in check_list:
    if i > maximum:
        maximum = i

for i in range(len(check_list)):
    if check_list[i] == maximum:
        print(i+1, end=' ')