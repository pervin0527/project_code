"""
1부터 100사이의 자연수가 적힌 카드 N장.
같은 숫자의 카드가 여러 장 있을 수 있음. 이 중 3장을 뽑아
각 카드에 적힌 수를 합한 값을 기록하는데 3장으로 뽑을 수 있는 모든 경우를 기록.
기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하시오.
"""
import sys
# sys.stdin = open('섹션 2\\3. k번째 큰 수\\input.txt')

N, K = map(int, input().split())
list_N = list(map(int, input().split()))
# print(N, K)
# print(list_N)

result = set()
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            result.add(list_N[i] + list_N[j] + list_N[m])

final = list(result)
final.sort(reverse=True)
print(final[K-1])