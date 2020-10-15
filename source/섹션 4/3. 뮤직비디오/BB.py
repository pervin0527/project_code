import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\3. 뮤직비디오\\input.txt', 'r')

# N개의 곡이 라이브 순서 그대로 유지되서 DVD에 녹화된다.
# 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
# M개의 DVD에 모든 영상을 녹화하는데 DVD의 크기를 최소로하면서 M개 모두 같은 크기로 만들려고 한다.

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# print(N, M, arr)
# DVD의 크기를 최소로한다. M개의 DVD 모두 같은 크기로 하려고 한다.
lt = 1
rt = sum(arr)
largest = arr[N-1]
res = 0

def count(middle):
    cnt = 1
    total = 0
    for x in arr:
        if total + x > middle: # 조건!!!
            cnt += 1
            total = x

        else:
            total += x

    return cnt

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) <= M and mid >= largest:
        res = mid
        rt = mid - 1

    else:
        lt = mid + 1

print(res)