import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 3/2. 숫자만 추출/input.txt', 'r')s

s = input()

res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)