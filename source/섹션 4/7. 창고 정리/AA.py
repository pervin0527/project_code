import sys
sys.stdin = open('섹션 4/7. 창고 정리/input.txt')

L = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()
for i in range(m):
    a[L-1] -= 1
    a[0] += 1
    a.sort()

print(a[L-1] - a[0])