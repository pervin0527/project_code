"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로
합쳐 출력하는 프로그램을 작성하세요.
"""
import sys
# sys.stdin = open('섹션 3/4. 두 리스트 합치기/input.txt')

N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

res = []

ta, tb = 0, 0
while ta < N:
    if b[tb] > a[ta]:
        res.append(a[ta])
        ta += 1

    elif a[ta] > b[tb]:
        res.append(b[tb])
        tb += 1
        
    elif a[ta] == b[tb]:
        res.append(a[ta])
        ta += 1

for i in range(tb, M):
    res.append(b[i])

for i in res:
    print(i, end = ' ')