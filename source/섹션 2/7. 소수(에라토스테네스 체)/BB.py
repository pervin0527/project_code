import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/7. 소수(에라토스테네스 체)/input.txt', 'r')

N = int(input())
list_N = [0] * (N+1)
cnt = 0

for i in range(2, N+1):
    if list_N[i] == 0:
        cnt += 1

    for j in range(i, N+1, i):
        list_N[j] = 1

print(cnt)