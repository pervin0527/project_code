import sys
sys.stdin = open('C:/Users/user/project_code/source/섹션 2/10. 점수 계산/input.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))
# print(N, list_N)

cnt = score = 0

for i in list_N:
    if i == 1:
        cnt += 1
        score += cnt

    else:
        cnt = 0

print(score)