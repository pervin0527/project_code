import sys
# sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\6. 씨름선수\\input.txt', 'r')

# 지원자 수 N, N명의 키와 몸무게가 차례로 주어지는데
n = int(input())
a = []

for i in range(n):
    w, h = map(int, input().split())
    a.append((w, h))

# 다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나 무거운 지원자만 뽑는다.
a.sort(reverse=True)
# print(a)

max_height = a[0][0]
max_width = a[0][1]
cnt = 1

for i in range(1, n):
    h, w = a[i][0], a[i][1]

    if max_width < w:
        cnt += 1
        max_width = w

print(cnt)