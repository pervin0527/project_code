import sys
sys.stdin = open('섹션 6/9. 수열 추측하기/input.txt', 'r')

# 1부터 N까지의 숫자가 한 개씩 적혀있다.
# N이 4 : 가장 윗 줄에 3 1 2 4
# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하시오.
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit()

    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                check[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n # 순열 저장
    b = [1] * n # 이항 계수 저장
    check = [0] * (n + 1)

    # n 값에 따라 변동하는 이항 계수 계산
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i

    DFS(0, 0)