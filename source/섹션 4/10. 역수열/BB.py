import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\10. 역수열\\input.txt', 'r')
n = int(input())
a = list(map(int, input().split()))
# print(n, a)

# 역수열이 주어졌을 때 원래의 수열을 출력하는 프로그램을 작성하세요.
# 원래의 수열은 1부터 n까지의 수를 한번씩만 사용하여 이루어짐.
seq = [0] * n

for i in range(n):
    for j in range(n):
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')
