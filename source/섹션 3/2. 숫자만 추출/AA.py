"""
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여
그 순서대로 자연수를 만듭니다. 만들어진 자연수와 그 자연수의 약수의 개수를 출력합니다.
만약 “t0e0a1c2h0er"에서 숫자만 추출하면 0, 0, 1, 2, 0이고
이것을 자연수로 만들면 120이 됩니다.
즉, 첫 자리 0은 자연수화 할 때 무시합니다.
"""
import sys
# sys.stdin = open('./섹션 3/2. 숫자만 추출/input.txt')

a = input()
tmp = 0

for i in a:
    if i.isdigit():
        tmp = tmp * 10 + int(i)
    else:
        pass

print(tmp)

cnt = 0
for i in range(1, tmp + 1):
    if tmp % i == 0:
        cnt += 1

print(cnt)