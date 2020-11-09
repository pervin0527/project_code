import sys
sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\1. 가장 큰 수\\input.txt", "r")

num, m = map(int, input().split())
num = list(map(int, str(num)))
print(num)

# stack을 사용. Last In First Out
# 들어가는 입구와 나오는 출구가 같다(한 곳이다.)
# 리스트를 가지고 append()를 써서 넣고, pop()을 해서 꺼낸다.

stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x: # stack이 비어있지 않고, m이 0이 아니면서 stack의 가장 뒷 자료가 x보다 작을 경우
        stack.pop()
        m -= 1

    stack.append(x)

if m != 0:
    stack = stack[ : -m]

res = "".join(map(str, stack))
print(res)