import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\2. 랜선자르기\\input.txt', 'r')
K, N = map(int, input().split())

# K개의 길이가 제각각인 랜선
# 길이가 모두 같은 N개의 랜선으로 만들고 싶다. N보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
# 만들 수 있는 최대 랜선의 길이를 구하시오.

arr = []
for i in range(K):
    value = int(input())
    arr.append(value)

arr.sort()

def count(middle):
    cnt = 0
    for x in arr:
        result = x // middle
        cnt += result

    return cnt

# N개 중 하나의 랜선의 길이는 최소 1cm에서 최대 k 중 가장 긴 랜선의 길이를 넘지 않는다.
lt = 1
rt = arr[K-1]
res = 0

while lt <= rt:
    mid = (lt + rt) // 2

    if count(mid) >= N:
        res = mid
        lt = mid + 1

    else:
        rt = mid - 1

print(res)