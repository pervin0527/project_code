import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/7. 사과나무/input.txt', 'r')
N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]

print(N, list_N)
start = end = bp = N // 2
result = 0

for i in range(N):
    for j in range(start, end+1):
        result += list_N[i][j] 

    if i < bp:
        start -= 1
        end += 1

    else:
        start += 1
        end -= 1

print(result)