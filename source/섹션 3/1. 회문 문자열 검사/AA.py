import sys

n = int(input())

for i in range(n):
    s = input() # 문자열 입력.
    s = s.upper()

    size=len(s)

    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break

    else:
        print("#%d YES" %(i+1))


"""
# line 9 ~ 17을 아래와 같이 변경해도 동작함.
if s==s[::-1]:
    print("#%d YES" %(i+1))

else:
    print("#%d NO" %(i+1))
"""
    