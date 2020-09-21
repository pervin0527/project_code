import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/7. 사과나무/input.txt', 'r')
N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]

res = 0

s=e=N//2

for i in range(N):
    for j in range(s, e+1):
        res+=list_N[i][j]
    if i < N//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)