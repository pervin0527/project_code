import sys

sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\3. 후위표기식 만들기\\input.txt", "r")
a = input()
stack = []
res = ""

for x in a:
    if x.isdecimal():
        res += x

    else:
        if x == '(':
            stack.append(x)

        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()

            stack.append(x)

        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()

            stack.append(x)

        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            
            stack.pop()

while stack:
    res+=stack.pop()


print(res)