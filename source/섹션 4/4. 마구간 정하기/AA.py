"""
N개의 마구간이 수직선상에 있을 때 각 마구간은
x1, x2, x3 ... xN의 좌표를 가지며 마구간 간에 좌표 중복은 없습니다.
C마리의 말이 있는데, 각 마구간에 한 마리의 말만 넣을 수 있습니다.
또한 가장 가까운 두 말의 거리가 최대가 되도록 배치하고 싶습니다.
C마리의 말을 N개 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가
되는 최대 값을 출력하는 프로그램을 작성하세요
"""
import sys
# sys.stdin = open('섹션 4/4. 마구간 정하기/input.txt')

N, C = map(int, input().split())
a = []

for x in range(N):
    a.append(int(input()))

a.sort()

start = 1
end = a[-1]
# print(start, end)

result = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    ep = a[0]

    for i in range(1, N):
        if a[i] - ep >= mid:
            cnt += 1
            ep = a[i]

    if cnt >= C:
        start = mid + 1
        result = mid

    else:
        end = mid - 1 

print(result)