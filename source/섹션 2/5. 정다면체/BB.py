import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/5. 정다면체/input.txt', 'r')

N, M = map(int, input().split())
# print(N, M)
result = [0] * (N+M+1)

# 두 주사위 눈의 합에 대해서 가장 높은 확률이 나오는 합이 무엇인지 구함.
for i in range(1, N+1): # 주사위의 눈은 1부터 시작하고 N까지
    for j in range(1, M+1):
        result[i+j] += 1

# 가장 높은 확률의 합이 무엇인지 구함.
maximum = 0

for i in range(1, len(result)):
    if result[i] >= maximum:
        maximum = result[i]

# 가장 높은 확률을 가지고 있는 인덱스 값들을 출력.
# 정답이 여러개일 경우 오름차순으로 출력함. 루프에서 이미 오름차순으로 탐색하기 때문에 추가 정렬 필요 없음.
for i in range(1, len(result)):
    if maximum == result[i]:
        print(i, end = ' ')