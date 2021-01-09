"""
지도 정보가 N*N 격자판에 주어집니다.
각 격자에는 그 지역의 높이가 적혀있습니다. 각 격자판의 숫자 중
자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리가 몇 개 있는지 출력하세요.
격자의 가장자리는 0으로 초기화 되었습니다.
"""
import sys
sys.stdin = open('섹션 3/9. 봉우리/input.txt')

N = int(input())
a = [list(map(int, input().split())) for i in range(N)]
# print(a)

a.insert(0, [0] * N)
a.append([0] * N)

for i in a:
    i.insert(0, 0)
    i.append(0)

# for i in a:
#     print(i)

cnt = 0
q = [-1, 0, 1, 0]
p = [0, 1, 0, -1]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if all(a[i][j] > a[i+q[k]][j+p[k]] for k in range(4)):
            cnt += 1

print(cnt)
