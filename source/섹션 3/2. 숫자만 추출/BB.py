import sys

sys.stdin = open('C:/Users/user/project_code/source/섹션 3/2. 숫자만 추출/input.txt', 'r')

a = input()
res = cnt = 0

for i in a:
    if i.isdecimal():
        res = res * 10 + int(i)

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)