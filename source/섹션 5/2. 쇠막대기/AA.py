import sys
# sys.stdin = open('섹션 5/2. 쇠막대기/input.txt')

a = input()
# print(a)

stack = []
total = 0
for x in range(len(a)):
    if a[x] == '(':
        stack.append(a[x])

    else:
        if a[x-1] == '(':
            stack.pop()
            total += len(stack)

        else:
            stack.pop()
            total += 1

print(total)