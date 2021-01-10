import sys
sys.stdin = open('섹션 4/10. 역수열/input.txt')

n = int(input())
a = list(map(int, input().split()))

t = [0] * n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and t[j] == 0:
            t[j] = i + 1
            break

        elif t[j] == 0:
            a[i] -= 1

for x in t:
    print(x, end=' ')