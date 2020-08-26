# 두 개의 정 N면체와 정 M면체 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를
# 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

# 입력 - 첫 번째 줄에는 자연수 N과 M이 주어집니다.
# N과 M은 4, 6, 8, 12, 20 중 하나입니다.

# 출력 - 첫 번째 줄에 답을 출력합니다.

import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/5. 정다면체/in1.txt')

N, M = map(int, input().split())
# print(N, M)

cnt_list = [0] * (N+M+1)

for i in range(1, N+1): # 주사위는 1부터 시작하고 N 값도 나와야 하기 때문에 N+1
    for j in range(1, M+1):
        idx = i + j
        cnt_list[idx] += 1 # 해결 방법 몰랐음.

maximum = 0

for i in range(N+M+1): # list 인덱스 값은 0부터 시작하니까 0 ~ 9라 10은 카운팅 못해서 + 1 해줌.
    tmp = cnt_list[i]

    if tmp >= maximum:
        maximum = tmp

for i in range(N+M+1):
    if cnt_list[i] == maximum:
        print(i, end=' ')