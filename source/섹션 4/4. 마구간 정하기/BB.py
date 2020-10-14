import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\4. 마구간 정하기\\input.txt', 'r')

N, C = map(int, input().split())

coord = []
for _ in range(N):
    tmp = int(input())
    coord.append(tmp)
coord.sort()

# 두 말의 거리가 최대가 되는 값을 구하는 문제니까
# 최소 값은 두 말이 간격 1만큼 두고 배치되는 경우, 최대 값은 coord 내의 가장 큰 값 - 가장 작은 값.
start = 1
end = coord[N-1] - coord[0]

def count(len):
    cnt=1
    ep=coord[0]
    for i in range(1, N):
        if coord[i]-ep>=len:
            cnt+=1
            ep=coord[i]
    return cnt

while start <= end: # 값이 같아지면 그 값이 정답.
    mid = (start + end) // 2

    if count(mid) >= C:
        res = mid
        start = mid + 1

    else:
        end = mid - 1  # C마리의 말을 채우지 못하니까 mid 보다 큰 값은 답이 될 수 없으므로 범위를 축소

print(res)