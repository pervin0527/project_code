import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/4. 두 리스트 합치기/input.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

# sort()를 사용하면 nlog(n)
# 입력 자체가 이미 정렬이 되어있는 상황을 합치는 것은 n번만에 실행됨
# nlog(n)과 n은 엄청난 차이가 있음 따라서 n번만에 실행되는 방법으로 풀어야함.

p1=p2=0
list_result = []

while p1<N and p2<M: # 리스트 중 하나의 포인터가 끝까지 갔을 때 종료
    if list_N[p1] <= list_M[p2]:
        list_result.append(list_N[p1])
        p1+=1

    else:
        list_result.append(list_M[p2])
        p2+=1


if p1<N:
    list_result = list_result + list_N[p1:]

if p2<M:
    list_result = list_result + list_M[p2:]

for x in list_result:
    print(x, end=' ')