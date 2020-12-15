import sys
sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 6\\4. 합이 같은 부분집합\\input.txt")

def DFS(L, sum):
    # L 은 리스트 a를 참조하는 인덱스 번호
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 종료

    else:
        DFS(L + 1, sum + a[L]) # L이 현재 가리키고 있는 a의 원소를 사용한다.
        DFS(L + 1, sum) # 사용하지 않고 이전 단계 값 그대로 가겠다.


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO") # 프로그램이 sys.exit(0)으로 종료되지 않으니 print문이 동작함.