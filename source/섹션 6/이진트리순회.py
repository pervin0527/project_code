import sys
# sys.stdin = open("", "r")

def DFS(v):
    if v > 7: # 7이 트리의 마지막 값이니까 종료
        return
    else:
        print(v, end=' ') # 전위 순회
        DFS(v * 2) # 왼쪽 자식 노드
        # print(v, end=' ') # 중위 순회
        DFS(v * 2 + 1) # 오른쪽 자식 노드
        # print(v, end=' ') # 후위 순회

if __name__ == "__main__":
    DFS(1)
