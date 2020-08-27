# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

# 입력설명 : 첫 줄에 자연수의 개수 N이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
# 3
# 125 15232 97

# 출력설명 : 자릿수의 합이 최대인 자연수를 출력한다.
# 97

import sys

def digit_sum(x):
    maximum = 0
    for idx, x in enumerate(list_N):
        str_score = str(x)
        
        tmp = 0
        for j in str_score:
            tmp += int(j)

        if tmp > maximum:
            maximum = tmp
            max_idx = idx

    return(max_idx)

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/6. 자릿수의 합/in1.txt')

N = int(input())
list_N = list(map(int, input().split()))

result = digit_sum(list_N)
print(list_N[result])