import sys
# sys.stdin = open('섹션 5/4. 후위식 연산/input.txt')

formula = input()
# print(formula)
stack = []
result = 0

for x in formula:
    if x.isdigit():
        stack.append(int(x))

    else:
        if x == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)

        elif x == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)

        elif x == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
        
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
     

print(stack[0])