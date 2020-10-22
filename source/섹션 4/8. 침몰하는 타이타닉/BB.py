import sys
sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\8. 침몰하는 타이타닉\\input.txt', 'r')

# N명의 승객. 구명보트는 2명이하만 탑승가능
# 보트 한 개에 탈 수 있는 총 무게도 M kg으로 제한되어 있다.
# N명의 승객 몸무게가 주어졌을 때 모두가 탈출하기 위한 구명보트의 최소 개수를 출력.
N, M = map(int, input().split())
list_N = list(map(int, input().split()))

# print(N, M, list_N)
list_N.sort()

cnt = 0
lt = 0
rt = N-1
while list_N:
    if len(list_N) == 1:
        cnt += 1
        break
    
    if list_N[0] + list_N[-1] > M:
        list_N.pop()
        cnt += 1

    else:
        list_N.pop(0)
        list_N.pop()
        cnt+=1

print(cnt)