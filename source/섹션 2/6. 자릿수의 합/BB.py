import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 2/6. 자릿수의 합/input.txt', 'r')

# 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력.

def digit_num(value):
    total = 0
    while value > 0:
        total += value % 10
        value = value // 10

    return total

N = int(input())
list_N = list(map(int, input().split()))

maximum = 0
for x in list_N:
    result = digit_num(x)

    if result > maximum:
        maximum = result
        anw = x

print(anw)
