"""
N개의 숫자로 이루어진 숫자열 중 s번째부터 e번째까지의 수를 오름차순 정렬했을 때
k번째로 나타나는 숫자를 출력하는 프로그램을 작성하시오.

첫번째 줄에 테스트 케이스 T가 주어지고, 각 케이스별
첫번째 줄은 자연수 N, s, e, k가 차례로 주어집니다.
두번째 줄에 N개의 숫자가 차례로 주어진다.
"""

import sys
# sys.stdin = open('섹션 2\\2. K번째 수\\input.txt')

T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    list_N = list(map(int, input().split()))
    # print(N, s, e, k)
    # print(list_N)

    # 주의할 점. s와 e는 인덱스 값이 1부터 시작하기 때문에 슬라이싱시 이를 고려.
    # 결과 출력도 마찬가지.
    res = list_N[s-1:e]
    res.sort()
    print("#%d %d" % (i+1, res[k-1]))