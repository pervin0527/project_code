import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/3. 카드 역배치/input.txt', 'r')

list_N = list(range(21))
# print(list_N)

for i in range(10):
    ai, bi = map(int, input().split())

    tmp = 0
    while ai < bi:
        tmp = list_N[bi]
        list_N[bi] = list_N[ai]
        list_N[ai] = tmp
        ai += 1
        bi -= 1

list_N.pop(0)

for i in list_N:
    print(i, end = ' ')