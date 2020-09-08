import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/10. 점수 계산/input.txt')

N = int(input())
list_N = list(map(int, input().split()))

sum = 0
cnt = 0

for x in list_N:
    if x == 1:
        cnt+= 1
        sum+=cnt

    else:
        cnt=0

print(sum)