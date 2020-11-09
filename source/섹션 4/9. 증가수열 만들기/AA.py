import sys
# sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\9. 증가수열 만들기\\input.txt', 'r')

# 1부터 N까지의 자연수로 구성된 길이 N의 수열.
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만든다.
# 이때 수열에서 가져온 숫자는 그 수열에서 제거된다.
N = int(input())
list_N = list(map(int, input().split()))

# 가장 왼쪽과 가장 오른쪽 값을 가리키는 변수들
lt = 0
rt = N - 1
tmp = [] # 현재 가장 왼쪽 값과 오른쪽 값을 저장하는 리스트
last = 0 # # 가장 최근에 증가 수열에 들어간 값.
result = ''

while lt <= rt:
    left = list_N[lt]
    right = list_N[rt]

    if last < left:
        tmp.append((left, "L"))

    if last < right:
        tmp.append((right, "R"))

    tmp.sort()

    if len(tmp) == 0: # last 값보다 작으면 tmp리스트에 추가될 수 없음. 즉, 더 이상 증가수열을 만들 수 없을 때.
        break

    else:
        last = tmp[0][0]
        result = result + tmp[0][1]

        if tmp[0][1] == "L":
            lt += 1

        else:
            rt -= 1

        tmp.clear()

print(len(result))
print(result)