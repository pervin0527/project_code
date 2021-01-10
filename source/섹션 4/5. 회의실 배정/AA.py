"""
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대해
회의실 사용표를 만들려고 합니다.
각 회의에 대해 시작 시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게
회의실을 사용할 수 있는 최대수의 회의를 찾으세요.
단, 회의는 한 번 시작하면 중간에 중단될 수 없으며, 한 회의가 끝나는 것과 동시에
다음 회의가 시작될 수 있습니다.
"""
import sys
# sys.stdin = open('섹션 4/5. 회의실 배정/input.txt')

n = int(input())
a = []

for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

## 포인트
a.sort(key = lambda x : (x[1], x[0]))
# for x in a:
#     print(x)

end_time = 0
cnt = 0

for start, end in a:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)