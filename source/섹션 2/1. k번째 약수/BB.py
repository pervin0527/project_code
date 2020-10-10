import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 2/1. k번째 약수/input.txt', 'r')
N, K = map(int, input().split())
# print(N, K)

# 약수 : N을 k로 나누었을 때 나머지가 0이면 k는 N의 약수
cnt = 0

for i in range(1, N+1): # 시작하는 값에서 나눗셈은 0으로는 불가능하기 때문에 1부터 시작. N 자신으로 나눈 값도 필요하니까 N+1
    if N % i == 0:
        cnt += 1

    if cnt == K:
        print(i)
        break

else:
    print(-1)

# for ~ else문
# for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고,
#끝까지 수행 되었을 때 수행하는 코드를 담고 있습니다.
