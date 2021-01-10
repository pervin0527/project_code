"""
K개의 랜선이 길이가 제각각으로 있습니다. 이를 모두 N개의 같은 길이의 랜선으로
만들고 싶기 때문에 K개의 랜선을 잘라서 만들어야 합니다.
편의를 위해 랜선을 자를때 손실되는 길이가 없다고 가정합니다.
또, N개보다 많이 만드는 것도 N개를 만드는 것에 포함됩니다.
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하세요.
"""
import sys
# sys.stdin = open('섹션 4/2. 랜선자르기/input.txt')

K, N = map(int, input().split())
A = []
maximum = 0

for i in range(K):
    tmp = int(input())
    A.append(tmp)
    maximum = max(maximum, tmp)

start = 1
end = maximum
result = 0

while start <= end:
    mid = (start + end) // 2

    val = 0
    for x in A:
        val += (x // mid)

    if val >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)