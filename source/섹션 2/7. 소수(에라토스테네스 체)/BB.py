# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다.

# 입력설명
# 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
# 20

# 출력설명
# 첫 줄에 소수의 개수를 출력합니다.
# 8

# 소수는 약수가 1과 자기 자신만 있을 때.
# 약수를 구하는 것은 나누기 했을 때 나머지가 0인 수

import sys
sys.stdin = open('C:/Users/user/project_code/source/섹션 2/7. 소수(에라토스테네스 체)\in2.txt', 'r')

N = int(input())
# N = 20
# print(N)

cnt = 0
for i in range(2, N+1):
    idx = 0
    for j in range(1, i+1):
        if i % j ==0:
            idx += 1

    if idx == 2:
        cnt += 1

print(cnt)
            