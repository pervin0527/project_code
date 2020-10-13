import sys
sys.stdin = open('C:/Users/user/project_code/source/섹션 3/10. 스도쿠 검사/input.txt', 'r')

list_N = [list(map(int, input().split())) for _ in range(9)]

"""
각 행에 1부터 9까지의 숫자가 중복 없이 나오고
각 열에 1부터 9까지의 숫자가 중복 없이 나오고
각 3 x 3짜리 사각형에 1부터 9까지의 숫자가 중복 없이 나옴.
"""
def check(list_N):
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10

        for j in range(9):
            row_check[list_N[i][j]] = 1
            col_check[list_N[j][i]] = 1

        if sum(row_check) != 9 and sum(col_check) != 9:
            return(False)

    for i in range(3):
        for j in range(3):
            block_check = [0] * 10

            for a in range(3):
                for b in range(3):
                        block_check[list_N[i * 3 + a][j * 3 + b]] = 1

            if sum(block_check) != 9:
                return(False)

    return(True)

if check(list_N):
    print("YES")

else:
    print("NO")