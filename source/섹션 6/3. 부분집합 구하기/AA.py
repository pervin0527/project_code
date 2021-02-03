import sys
sys.stdin = open('섹션 6/3. 부분집합 구하기/input.txt')

def DFS(x):
    if x == n + 1:
        for i in range(n + 1):
            if ch[i] == 1:
                print(i, end = ' ')

        print()

    else:
        ch[x] = 1 # 해당 원소를 부분집합으로 사용하겠다.
        DFS(x + 1)
        ch[x] = 0
        DFS(x + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)