import sys

def reverse(x):
    res = 0
    while x > 0:
        remainder = x % 10
        res = res * 10 + remainder
        x = x // 10

    return res

def isPrime(reversed_n):
    if reversed_n == 1:
        return False

    for i in range(2, reversed_n//2+1):
        if reversed_n % i == 0:
            # print(reversed_n, i)
            return False

    else:
        return True


# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/8. 뒤집은 소수/input.txt', 'r')
N = int(input())
list_N = list(map(int, input().split()))

for x in list_N:
    reversed_x = reverse(x)
    if isPrime(reversed_x):
        print(reversed_x, end = ' ')
    