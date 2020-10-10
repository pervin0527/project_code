import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 2/3. k번째 큰 수/input.txt', 'r')

N, K = map(int, input().split())
list_N = list(map(int, input().split()))
# print(N, K, list_N)

result = set() # set함수는 중복을 제거하는 함수. 순서대로 정렬되지 않음.

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            result.add(list_N[a] + list_N[b] + list_N[c]) # set은 딕셔너리 타입이므로 append가 아니라 add를 통해 1개 값을 삽입함.

# print(result)
result = list(result) # dict 타입을 list타입으로 변경
result.sort(reverse=True) # 값이 정렬되지 않은 상태이기 때문에 내림차순으로 정렬함.
print(result[K-1]) # k번째로 큰 값을 출력. 인덱스는 0부터 시작하기 때문에 k-1
