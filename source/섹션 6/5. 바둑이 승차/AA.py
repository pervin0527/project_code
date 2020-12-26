import sys
# sys.stdin = open("source\\섹션 6\\5. 바둑이 승차\\input.txt")

def DFS(L, sum, tsum):
    global result
    if sum + (total - tsum) < result:
        return

    if sum > c:
        return

    if L == n:
        if sum > result:
            result = sum

    else:
        DFS(L + 1, sum + a[L], tsum + a[L])
        DFS(L + 1, sum, tsum + a[L])


if __name__ == "__main__":
    c, n= map(int, input().split())
    result = -10000000000000
    a = [0] * n
    for i in range(n):
        a[i] = int(input())

    total = sum(a)
    DFS(0, 0, 0)
    print(result)