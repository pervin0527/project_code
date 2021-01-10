"""
임의의 N개 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한개의 수인 M이 주어지면
이분 검색으로 M이 정렬된 상태에서 몇번째에 있는지 구하세요.
중복값은 존재하지 않습니다.
"""
import sys
# sys.stdin = open('섹션 4/1. 이분검색/input.txt')
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(N, M, A)

start = 0 
end = N - 1

while start <= end:
    mid = (start + end) // 2

    if A[mid] == M:
        print(mid + 1)
        break

    elif A[mid] > M:
        end = mid - 1

    else:
        start = mid + 1