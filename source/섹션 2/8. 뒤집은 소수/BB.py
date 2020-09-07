import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 2/8. 뒤집은 소수/in1.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))

def reverse(n):
    res=0
    while n > 0:
        t = n % 10
        n = n // 10
        res = res * 10 + t

    return res

def isPrime(reversed_n):
    if reversed_n == 1:
        return False

    for i in range(2, reversed_n//2+1):
        if reversed_n % i == 0:
            return False

    else:
        return True

for i in list_N:
    reversed_n = reverse(i)
    if isPrime(reversed_n) == True:
        print(reversed_n, end=' ')