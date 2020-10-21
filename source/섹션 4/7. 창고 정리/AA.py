import sys
# sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\7. 창고 정리\\input.txt','r')

# 창고의 가로 길이 L, L개의 자연수가 공백을 사이에 두고 입력된다. 높이 조정횟수인 M
L = int(input())
list_L = list(map(int, input().split()))
M = int(input())

# 창고 높이 조정은 가장 높은 곳에서 가장 낮은 곳으로 이동하는 것을 말한다.
# 가장 높은 곳이나 가장 낮은 곳이 여러 곳이면 그 중 아무거나 선택하면 된다.
# M회의 높이 조정을 한 후 가장 높은 곳과 가장 낮은 곳의 차이를 출력하시오.
# print(list_L)
list_L.sort()
for i in range(M):
    list_L[0] += 1
    list_L[L-1] -= 1
    list_L.sort()

print(list_L[L-1] - list_L[0])