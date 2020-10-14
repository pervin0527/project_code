import sys

sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\3. 뮤직비디오\\input.txt', 'r')

# 총 N개의 곡이 라이브 순서 그대로 DVD에 들어간다.
# 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
# M개의 DVD에 모든 동영상을 녹화하려 하는데 DVD의 크기를 최소로 하며,
# M개의 DVD는 모두 같은 크기여야 한다.
N, M = map(int, input().split())

# 라이브에서 부른 순서대로 부른 곡의 길이가 분 단위로 주어진다.
list_N = list(map(int, input().split()))
# print(N, M, list_N)

# DVD의 최소 용량 크기를 구하시오.
start = 1
end = sum(list_N)

while start <= end:
    mid = (start + end) // 2
    
    cnt = total = 0
    for x in list_N:
        if total + x > mid:
            cnt += 1
            total = x
        
        else:
            total += x