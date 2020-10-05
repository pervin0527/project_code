import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/9. 봉우리/input.txt', 'r')

N = int(input())
list_N = [list(map(int, input().split())) for _ in range(N)]

list_N.insert(0, [0] * N)
list_N.append([0] * N)
print(list_N)

for x in list_N:
    x.insert(0, 0)
    x.append(0)

print(list_N)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(list_N[i][j] > list_N[i+dx[k]][j+dy[k]] for k in range(4)): # all()는 인자 값이 모두 참일 때 참을 반환함.
            cnt += 1

print(cnt)
        