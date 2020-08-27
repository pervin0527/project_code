import sys

def digit_num(x):
    sum = 0
    while x > 0:
        tot = x % 10
        x = x // 10
        sum += tot
    return sum

sys.stdin = open('C:/Users/user/project_code/source/섹션 2/6. 자릿수의 합/in1.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))

max = 0
for i in list_N:
    tot = digit_num(i)

    if tot > max:
        max = tot
        ans = i

print(ans)
