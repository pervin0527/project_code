import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 4/1. 이분검색/input.txt', 'r')

N, M = map(int, input().split())
list_N = list(map(int, input().split()))

list_N.sort() # 오름차순 정렬
print(N, M, list_N)

start = 0
end = N - 1


while start<=end:
    mp = (start + end) // 2
    if list_N[mp] == M:
        print(mp+1)
        break

    elif list_N[mp] > M:
        end = mp - 1

    elif list_N[mp] < M:
        start = mp + 1