import sys
sys.stdin = open('섹션 6/4. 합이 같은 부분집합/input.txt')

def DFS(i, sum): # i는 리스트 a의 인덱스 번호, sum은 현재 원소를 부분집합에 포함하는 여부
    if sum > total // 2: # 이미 total의 절반 값보다 큰 값이라면 그 다음 단계 합은 할 필요가 없으므로 return한다.
        return

    if i == n:
        if (total - sum) == sum:
            print("YES")
            sys.exit(0) # python 프로그램을 종료하겠다.

    else:
        DFS(i + 1, sum + a[i])
        DFS(i + 1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    # print(total)

    DFS(0, 0)
    # sys.exit(0)으로 종료되지 않았고, 마지막 재귀호출까지 끝내버리고 난 경우
    # 이 원소들로는 부분 집합 합이 같아 질 수 없으므로 No를 출력
    print("NO")
