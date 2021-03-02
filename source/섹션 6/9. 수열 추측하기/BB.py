import sys
sys.stdin = open('섹션 6/9. 수열 추측하기/input.txt', 'r')

def DFS(level, sum):
    if level == n and sum == f:
        for x in permutation:
            print(x, end=' ')
        sys.exit(0)

    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                permutation[level] = i
                DFS(level + 1, sum + (permutation[level] * rank[level]))
                check[i]=0

if __name__ == "__main__":
    n, f = map(int, input().split())
    permutation = [0] * n
    rank = [1] * n
    check = [0] * (n + 1)

    for i in range(1, n-1):
        rank[i] = rank[i-1] * (n-i) // i

    DFS(0, 0)