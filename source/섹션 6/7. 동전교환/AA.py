import sys
sys.stdin = open('섹션 6/7. 동전교환/input.txt')

def DFS(level, sum):
    global max
    if sum > m:
        return

    if sum == m:
        if level < max:
            max = level

    else:
        for i in range(n):
            DFS(level + 1, sum + a[i])
            
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    max = 2147000000

    a.sort(reverse=True)
    DFS(0, 0)

    print(max)