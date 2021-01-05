import sys
# sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 6\\8. 순열 구하기\\input.txt')

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')

        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * n
    ch = [0] * (n + 2)
    # print(n, m)

    DFS(0)
    print(cnt)