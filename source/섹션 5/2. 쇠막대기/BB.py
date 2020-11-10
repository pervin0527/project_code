import sys
sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\2. 쇠막대기\\input.txt", "r")

s = input()
cnt = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])

    else:
        if s[i-1] == '(':
            stack.pop()
            cnt += len(stack)

        else:
            stack.pop()
            cnt += 1

print(cnt)