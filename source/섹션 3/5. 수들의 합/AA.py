import sys
# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/5. 수들의 합/input.txt','r')

N, M = map(int, input().split())
list_N = list(map(int, input().split()))

lt = 0
rt = 1
tot = list_N[0]
cnt = 0

while True:
    if tot < M:
        if rt < N:
            tot += list_N[rt]
            rt += 1

        else:
            break

    elif tot == M:
        cnt += 1
        tot -= list_N[lt]
        lt += 1

    else:
        tot -= list_N[lt]
        lt += 1

print(cnt)