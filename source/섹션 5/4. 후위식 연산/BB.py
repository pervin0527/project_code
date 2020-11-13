import sys

sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\4. 후위식 연산\\input.txt", 'r')
a = input()
# print(a)

stack = []

for i in a:
    if i.isdecimal():
        stack.append(int(i))

    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if i == "+":
            tmp = num1 + num2

        elif i == "-":
            tmp = num1 - num2

        elif i == "*":
            tmp = num1 * num2

        elif i == "/":
            tmp = num1 / num2
        
        stack.append(tmp)

print(stack[0])