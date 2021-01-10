"""
현수는 씨름 선수 선발 공고를 냈고 N명의 지원자가 지원을 했습니다.
각 지원자의 키와 몸무게 정보를 알고 있는데, 다른 모든 지원자와
일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나 무거운 지원자만 뽑기로
했습니다.
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A는 탈락입니다.
"""
import sys
# sys.stdin = open('섹션 4/6. 씨름선수/input.txt')

n = int(input())
a = []

for i in range(n):
    weight, tall = map(int, input().split())
    a.append((weight, tall))

a.sort(key=lambda x: x[0], reverse=True)
# print(a)

cnt = 0
max_weight = 0
for _, weight in a:
    if weight > max_weight:
        max_weight = weight
        cnt += 1

print(cnt)