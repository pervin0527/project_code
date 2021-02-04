import sys
# sys.stdin = open('섹션 6/5. 바둑이 승차/input.txt')

def DFS(level, total, tsum):
    global maximum

    if total + (total_w - tsum) < maximum:
        return

    if total > c:
        return

    if level == n:
        if total > maximum:
           maximum = total

    else:
        DFS(level + 1, total + weight[level], tsum + weight[level])
        DFS(level + 1, total, tsum + weight[level])

if __name__ == "__main__":
    c, n = map(int, input().split())
    weight = []
    maximum = 0
    
    for i in range(n):
        w = int(input())
        weight.append(w)
    
    total_w = sum(weight)

    DFS(0, 0, 0)
    print(maximum)