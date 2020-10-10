import sys
# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/4. 대표값/input.txt', 'r')

N = int(input())
list_N = list(map(int, input().split()))

# 평균을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 인가?
avg = sum(list_N) / N
avg = int(avg + 0.5)

minimum = float('inf') # 값을 무한대로 설정해서 초기화
for idx, value in enumerate(list_N):
    tmp = abs(avg - value)

    if tmp < minimum: # 현재 인덱스의 값이 최소값보다 작으면 최소값 초기화.
        minimum = tmp
        score = value
        number = idx + 1

    elif tmp == minimum: # 현재 인덱스의 값과 최소값이 같으면 문제에서 성적이 높은 학생의 번호를 출력하라고 해두었음.
        if value > score: # 이 if문에서 답이 여러개 일때 즉, 동일한 값이 여러개일 때는 빠른 학생의 번호를 출력하라고 했으니까 넘어가게 됨.
            score = value
            number = idx + 1

print(avg, number)