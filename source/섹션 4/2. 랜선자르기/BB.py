import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\2. 랜선자르기\\input.txt', 'r')
K, N = map(int, input().split())

# K개의 랜선으로 길이가 모두 같은 N개의 랜선을 얻으려고 한다. 이때 길이가 최대 몇인지?
# N보다 많이 만드는 것도 N개를 만드는 것에 포함된다.

list_K = []
largest = 0
res = 0

# 잘랐을 때 최대 길이는 K개의 랜선 중 최대 길이를 넘지 않으므로 탐색 범위를 1cm ~ K 중 가장 길이가 긴 랜선의 값으로 지정.
for i in range(K):
    tmp = int(input())
    list_K.append(tmp)
    largest = max(largest, tmp)
    
# 이분 검색으로 N 이상이 되는 값을 탐색.
start = 1
end = largest

while start <= end:
    mp = (start + end) // 2

    cnt = 0
    for x in list_K:
        cnt += (x // mp)

    if cnt >= N:
        res = mp
        start = mp + 1

    else:
        end = mp - 1

print(res)