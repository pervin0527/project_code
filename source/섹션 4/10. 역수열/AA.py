import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\10. 역수열\\input.txt', 'r')

# 1부터 n까지의 수를 한번씩만 사용하여 이루어진 수열이 있다.
# 1부터 n까지 각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것이 역수열
# 자연수 n과 역수열이 주어질때 원래의 수열을 구하시오.

N = int(input())
list_N = list(map(int, input().split()))

result = [0] * N

for i in range(N):
    for j in range(N):
        if list_N[i] == 0 and result[j] == 0:
            result[j] = i + 1
            break

        elif result[j]==0:
            list_N[i] -= 1

for x in result:
    print(x, end=' ')