import sys
# sys.stdin = open('/mnt/c/Users/user/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 6/10. 조합 구하기/input.txt')

def DFS(level, start):
    global cnt
    if level == m:
        for j in range(m):
            print(res[j], end=' ')
        cnt += 1
        print()

    else:
        for i in range(start, n+1):
            res[level] = i
            DFS(level + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    DFS(0, 1)
    print(cnt)