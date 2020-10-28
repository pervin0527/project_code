import sys
sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\9. 증가수열 만들기\\input.txt', 'r')

# 1부터 N까지의 자연수로 구성된 길이 N의 수열
N = int(input())
list_N = list(map(int, input().split()))
# print(N, list_N)

lt = 0
rt = N - 1
last = 0
tmp = []
res = ''

while lt<=rt:
    if last < list_N[lt]:
        tmp.append((list_N[lt], 'L'))

    if last < list_N[rt]:
        tmp.append((list_N[rt], 'R'))

    tmp.sort()

    if len(tmp) == 0:
        break

    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)