import sys
sys.stdin=open("/mnt/c/Users/user/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 6/11. 수들의 조합/input.txt")
def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])
 
if __name__=="__main__":
    n, k=map(int, input().split())
    a=list(map(int, input().split()))
    m=int(input())
    cnt=0
    DFS(0, 0, 0)
    print(cnt)