# N개의 자연수가 입력되면 각 자연수를 뒤집은 후
# 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
# 예를 들어 32를 뒤집으면 23이고, 23은 소수니까 23을 출력.
# 단 910을 뒤집으면 19로 숫자화 해야한다.
# 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x)와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하세요.

# 입력설명
# 첫 줄에 자연수의 개수 N이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 5
# 32 55 62 3700 250

# 출력설명
# 첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
# 23 73

import sys
# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/8. 뒤집은 소수/in1.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))

# print(N)
# print(list_N)

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
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

for n in list_N:
    reversed_n = reverse(n)
    if isPrime(int(reversed_n)):
        print(reversed_n, end=' ')