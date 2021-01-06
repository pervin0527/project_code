"""
N개의 자연수가 입력되면 각 자연수를 뒤집은 후
그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
예를 들어 32를 뒤집으면 23이고, 23은 소수입니다. 따라서 23을 출력합니다.
단, 910을 뒤집으면 19로 변경해야 합니다.
첫 자리부터의 연속된 0은 무시합니다.
뒤집는 함수은 def reverse(x)와 소수 확인을 하는 def is_Prime(x)를 작성하세요.
"""
import sys
sys.stdin = open("섹션 2\\8. 뒤집은 소수\\in1.txt")

def reverse(x):
    v = 0
    while x > 0:
        r = x % 10
        x = x // 10
        v = v * 10 + r

    return v

def is_Prime(x):
    cnt = 0

    if x == 1:
        return False

    for i in range(2, x//2+1):
        if x % i == 0:
            return False

    else:
        return True

if __name__ == "__main__":
    N = int(input())
    list_N = list(map(int, input().split()))

    for i in list_N:
        reversed_i = reverse(i)
        if is_Prime(reversed_i):
            print(reversed_i, end = ' ')
