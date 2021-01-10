"""
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면
위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는
프로그램을 작성하세요.
구부러진 경우는 간주하지 않습니다.
"""
import sys
# sys.stdin = open('섹션 3/11. 격자판 회문수/input.txt')

a = [list(map(int, input().split())) for i in range(7)]
# for i in a:
#     print(i)

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        # print(tmp)
        
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(5//2):
            if a[i+k][j] != a[i+5-1-k][j]:
                break
        else:
            cnt += 1

print(cnt)