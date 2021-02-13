import sys
sys.stdin = open('섹션 6/8. 순열 구하기/input.txt')

def DFS(level):
    global cnt
    if level == m:
        for i in range(level):
            print(result[i], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                result[level] = i
                DFS(level+1)
                check[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [0] * (n + 1)
    result = [0] * n
    cnt = 0

    DFS(0)
    print(cnt)