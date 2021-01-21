import sys
sys.stdin = open('섹션 5/8. 단어찾기/input.txt')

n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

# print(p)

for i in range(n-1):
    word = input()
    p[word] = 0

for key, value in p.items():
    if value == 1:
        print(key)
        break