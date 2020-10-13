import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/4. 두 리스트 합치기/input.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

p1 = p2 = 0
res = []

while p1 < N and p2 < M:
    if list_N[p1] < list_M[p2]:
        res.append(list_N[p1])
        p1 += 1

    elif list_N[p1] > list_M[p2]:
        res.append(list_M[p2])
        p2 += 1

    else:
        res.append(list_N[p1])
        p1 += 1

if p1 < N:
    res = res + list_N[p1:]

if p2 < M:
    res = res + list_M[p2:]

for i in res:
    print(i, end = ' ')