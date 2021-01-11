import sys
# sys.stdin = open('섹션 5/1. 가장 큰 수/input.txt')

n, m = map(int, input().split())
num = list(map(int, str(n)))
# print(num)

stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack=stack[:-m]

res=''.join(map(str, stack))
print(res)