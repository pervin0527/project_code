import sys
# sys.stdin = open('섹션 5/3. 후위표기식 만들기/input.txt')

formula = input()
stack = []
res = ''

for x in formula:
    if x.isdigit():
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
    res += stack.pop()

print(res)