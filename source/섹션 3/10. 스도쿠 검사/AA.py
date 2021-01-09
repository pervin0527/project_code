"""
9 * 9 크기의 보드가 있을 때 각 행과 열 그리고 9개의 3 * 3 크기 보드에
1 ~ 9까지 숫자가 중복없이 나타나는 것이 스도쿠입니다.
입력된 스도쿠가 정확하게 풀렸으면 YES 그렇지 않으면 NO를 출력하세요.
"""
import sys
sys.stdin = open('섹션 3/10. 스도쿠 검사/input.txt')

def check(a):
    for i in range(9):
        ch_row = [0] * 10
        ch_col = [0] * 10

        for j in range(9):
            ch_row[a[i][j]] = 1
            ch_col[a[j][i]] = 1

        if sum(ch_row) != 9 or sum(ch_col) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch_block = [0] * 10
            for k in range(3):
                for l in range(3):
                    ch_block[a[i+k][j+l]] = 1

            if sum(ch_block) != 9:
                return False

            else:
                return True




if __name__ == "__main__":
    a = [list(map(int, input().split())) for x in range(9)]
    # for i in a:
    #     print(i)

    if check(a):
        print("YES")

    else:
        print("NO")