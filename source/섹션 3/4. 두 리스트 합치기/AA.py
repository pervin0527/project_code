import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/4. 두 리스트 합치기/input.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

result = list_N + list_M
result.sort()
print(result)