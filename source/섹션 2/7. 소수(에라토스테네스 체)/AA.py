"""
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
제한시간 1초입니다.
"""
import sys
# sys.stdin = open("섹션 2\\7. 소수(에라토스테네스 체)\\input.txt")

N = int(input())
check_list = [0] * (N + 1)
cnt = 0

# 소수는 1과 자기 자신으로밖에 나누어떨어지지 않는 1 이외의 정수.
for i in range(2, N+1):
    if check_list[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            check_list[j] = 1

print(cnt)