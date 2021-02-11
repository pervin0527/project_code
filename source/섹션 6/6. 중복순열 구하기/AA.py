import sys
sys.stdin = open('섹션 6/6. 중복순열 구하기/input.txt')

def DFS(x):
    global cnt

    if x == m:
        for i in range(m):
            print(check_list[i], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n + 1):
            check_list[x] = i
            DFS(x + 1)



if __name__ == "__main__":
    n, m = map(int, input().split())
    check_list = [0] * n
    cnt = 0

    DFS(0)
    print(cnt)