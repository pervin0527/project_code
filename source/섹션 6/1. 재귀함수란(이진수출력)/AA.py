import sys
# sys.stdin = open('섹션 6/1. 재귀함수란(이진수출력)/input.txt')

def recursive(x):
    if x == 0:
        return
    else:
        remain = x % 2
        recursive(x//2)
        print(remain, end='')

if __name__ == "__main__":
    n = int(input())
    recursive(n)