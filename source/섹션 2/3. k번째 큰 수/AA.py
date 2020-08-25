# 문제해석
# 1부터 100사이의 자연수가 적힌 N장의 카드 - 길이가 N인 list
# 같은 숫자의 카드가 여러장 있을 수 있다. - list내 중복된 숫자들이 있을 수 있다.
# 이 중 3장을 뽑아 카드에 적힌 수를 합한 값을 기록한다. - list에서 랜덤으로 3개의 값을 뽑아 합한 값을 기록
# 3장을 뽑을 수 있는 모든 경우를 기록 - 3개 합한 모든 경우의 수를 구함.
# 기록한 값 중 K번째로 큰 수를 출력 - 기록된 합들 중 K번째로 큰 값을 출력한다.

# 첫 줄에 자연수 N과 K가 입력된다. 그 다음 줄에 N개의 카드 값이 입력
# 첫 줄에 K번째 수를 출력. K번째 수는 반드시 존재.

import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/3. k번째 큰 수/in1.txt')

N, K = map(int, input().split())

list_N = list(map(int, input().split()))

res = set() # 중복 제거할 때 사용. 순서가 없음.

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            res.add(list_N[a] + list_N[b] + list_N[c])

res = list(res)
res.sort(reverse=True)
print(res[K-1])


