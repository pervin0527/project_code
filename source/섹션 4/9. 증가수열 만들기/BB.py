import sys
sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\9. 증가수열 만들기\\input.txt', 'r')

# 1부터 N까지의 자연수로 구성된 길이 N의 수열
N = int(input())
list_N = list(map(int, input().split()))
print(N, list_N)

