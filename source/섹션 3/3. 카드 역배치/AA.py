import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/3. 카드 역배치/input.txt', 'r')

list_N = list(range(21))
# print(list_N)

for _ in range(10):
    a, b = map(int, input().split())
    
    for i in range((b - a + 1) // 2):
        list_N[a+i], list_N[b-i] = list_N[b-i], list_N[a+i]

list_N.pop(0)

for x in list_N:
    print(x, end= ' ')