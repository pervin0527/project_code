import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 4/1. 이분검색/input.txt', 'r')

# 임의의 N개의 숫자가 입력으로 주어짐. N개의 수를 오름차순으로 정렬하고
# N개의 수 중 한 개인 M이 주어지면 이분검색으로 M이 몇 번째에 있는지 구하시오.
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() # 오름차순 정렬
# print(N, M, arr)

lt = 0
rt = N-1

while lt <= rt:
    mid = (lt + rt) // 2

    if arr[mid] == M:
        print(mid+1)
        break

    elif arr[mid] < M: # 현재 mid 값보다 M의 값이 더 크다면 mid보다 작은 위치에 있는 값들은 정답이 될 수 없기 때문에 시작 지점을 mid + 1로 바꾼다.
        lt = mid + 1

    elif arr[mid] > M: # 현재 mid 값보다 M의 값이 더 작다면 mid보다 큰 위치에 있는 값들은 정답이 될 수 없기 때문에 종료 지점을 mid - 1로 바꾼다.
        rt = mid - 1    