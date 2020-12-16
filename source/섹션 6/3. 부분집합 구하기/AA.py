import sys

# sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 6\\3. 부분집합 구하기\\input.txt", "r")

def DFS(v):
    if v > n:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()

    else:
        ch[v] = 1 # 원소를 부분집합에 포함시키겠다.
        DFS(v + 1)

        ch[v] = 0 # 원소를 부분집합에 포함시키지 않겠다.
        DFS(v + 1)
        

if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)