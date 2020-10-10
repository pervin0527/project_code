import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/2. K번째 수/input.txt', 'r')
T = int(input())

for i in range(T): # T - 테스트 케이스 만큼 작업을 수행해야함.
    N, s, e, k = map(int, input().split())
    list_N = list(map(int, input().split()))

    result_N = list_N[s-1:e] # s부터 e까지 슬라이싱하는데 제시된 숫자들은 리스트 인덱스가 1부터 시작하는것으로 가정하고 있기 때문에 s-1로 해야함.
    result_N.sort()

    print("#%d %d" %(i+1, result_N[k-1]))