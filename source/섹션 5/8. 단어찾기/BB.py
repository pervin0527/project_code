import sys

sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 5\\8. 단어찾기\\input.txt", "r")

n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word]=1

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break