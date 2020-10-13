import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 3\\11. 격자판 회문수\\input.txt', 'r')
list_N = [list(map(int, input().split())) for _ in range(7)]

# print(list_N)

# 7*7 2차원 리스트에서 길이 5인 회문수가 몇 개 있는지 구하므로 3번째까지만 돌림.
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = list_N[j][i:i+5]
        # print(tmp)

        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):
            if list_N[i+k][j]!=list_N[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)