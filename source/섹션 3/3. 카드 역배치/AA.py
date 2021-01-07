"""
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 오름차순으로 한 줄로 놓여있습니다.
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
다음과 같은 규칙으로 위치를 바꿉니다. 구간 [a, b]가 주어지면 a부터 b까지의 현재의
역순으로 놓습니다.

예를들어 [5, 10]으로 주어진다면, 위치 5부터 위치 10까지의 카드
5 6 7 8 9 10을 역순으로 10 9 8 7 6 5로 놓습니다.

총 10개의 줄에 걸쳐 한 줄에 하나씩 총 10개의 구간이 주어집니다.
"""
import sys
# sys.stdin = open('섹션 3/3. 카드 역배치/input.txt')

numbers = list(x for x in range(0, 21))
# print(a)

for i in range(10):
    a, b = map(int, input().split())
    # print(a, b)

    iter = int((b-a)/2) + 1
    for j in range(iter):
        # print((a+j), (b-j))
        numbers[a + j], numbers[b - j] = numbers[b - j], numbers[a + j]

for i in range(1, 21):
    print(numbers[i], end = ' ')