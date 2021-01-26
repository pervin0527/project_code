def DFS(x):
    if x > 7:
        return
    else:
        print(x, end=' ') # 전위 순회
        DFS(x * 2)
        # print(x, end=' ') # 중위 순회
        DFS(x * 2 + 1)
        # print(x, end=' ') # 후위 순회 

if __name__ == "__main__":
    DFS(1)