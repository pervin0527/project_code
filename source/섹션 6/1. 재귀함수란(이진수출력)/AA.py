import sys
# sys.stdin = open("C:\\Users\\user\\project_code\\source\\섹션 6\\1. 재귀함수란(이진수출력)\\input.txt", "r")

def recursive(x):
    if x == 0:
        return # 함수를 그냥 종료 시키겠다는 의미.

    else:
        recursive(x // 2)
        print(x % 2, end='')


if __name__ == "__main__":
    n = int(input())
    recursive(n)