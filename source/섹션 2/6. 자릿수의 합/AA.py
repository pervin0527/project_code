"""
N개의 자연수가 입력되면 각 자연수의 자릿수 합을 구하고
그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.
단, 자릿수의 합을 구하는 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
"""
import sys
# sys.stdin = open('섹션 2\\6. 자릿수의 합\\input.txt')


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += (x % 10)
        x = x // 10

    return sum
    

if __name__ == "__main__":
    N = int(input())
    list_N = list(map(int, input().split()))
    # print(N, list_N)

    maximum = -2147000000

    for i in list_N:
        tmp = digit_sum(i)
        if tmp > maximum:
            maximum = tmp
            result = i

    print(result)        