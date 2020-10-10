import sys

# sys.stdin = open('C:/Users/user/project_code/source/섹션 2/9. 주사위 게임/input.txt', 'r')

res=0
n=int(input())
for i in range(n):
    tmp=input().split()
    # print(tmp)
    tmp.sort() 
    a, b, c=map(int, tmp)
    if a==b and b==c:
        money=10000+(a*1000);
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res:
        res=money

print(res)