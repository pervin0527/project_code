"""
DVD에는 총 n개의 곡이 들어가는데 DVD에 녹화되는 라이브는 순서가 그대로
유지되어야 합니다.
즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의
모든 노래도 같은 DVD에 녹화해야 합니다.
또한, 두 개의 DVD에 나눠서 녹화하면 안됩니다.
M개의 DVD에 모든 동영상을 녹화하려 할때 DVD의 크기는 최소로 하려고 합니다.
그리고 M개의 DVD는 크기가 모두 같습니다.
이 때 DVD의 최소 용량 크기를 구하세요
"""
import sys
# sys.stdin = open('섹션 4/3. 뮤직비디오/input.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))
# print(N, M, A)

maximum = sum(A)
longest = max(A)
# print(maximum)

start = 1
end = maximum
result = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    tmp = 0
    for x in A:
        if tmp + x > mid:
            cnt += 1
            tmp = x
        else:
            tmp += x

    if mid >= longest and cnt <= M:
        end = mid - 1
        result = mid

    else:
        start = mid + 1

print(result)