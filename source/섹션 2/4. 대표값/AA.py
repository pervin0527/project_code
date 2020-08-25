# N명의 학생의 수학 성적이 주어진다. - N개의 값이 주어진다.
# N명의 학생들의 평균을 소수점 첫째자리 반올림으로 구하고. - N개 값의 평균을 구함. 소수점 첫째자리 반올림
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성
# 답이 2개일 경우, 성적이 높은 학생의 번호를 출력한다.
# 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.

# 입력 첫줄에 자연수 N이 주어지고, 두번째 줄에는 N개의 자연수가 주어짐
# 학생의 번호는 앞에서부터 1부터 N까지이다.

# 출력 첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력.
# 평균은 소수 첫째 자리에서 반올림

import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/4. 대표값/in1.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))

avg = round(sum(list_N) / N)

minimum = float('inf')
for idx, x in enumerate(list_N):
    tmp = abs(x - avg)

    if tmp < minimum:
        minimum = tmp
        score = x
        std_num = idx + 1

    elif tmp == minimum:
        if x > score:
            score = x
            std_num = idx + 1

print('%d %d' %(avg, std_num))
        
    