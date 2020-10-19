import sys
sys.stdin = open('C:\\Users\\user\\project_code\\source\\섹션 4\\5. 회의실 배정\\input.txt', 'r')

# 한 개의 회의실. n개의 회의
# 시작시간과 끝나는 시간이 주어지고, 회의실을 사용할 수 있는 최대수
n = int(input())

# 그리디 알고리즘 - 멀리 생각하지 않고 지금 당장의 단계에서 가장 최선의 선택을 하는 방법.
# 문제를 풀어나가는 과정 중 가장 좋은 결과를 나타내는 것이 무엇인지.
# 어떻게? - 정렬.
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) # tuple형태로 리스트에 입력

meeting.sort(key = lambda x : (x[1], x[0])) ### 앞에 오는 인자를 1순위로 정렬. 값이 같으면 뒤에 오는 인자를 기준으로 정렬

end_time = 0
cnt = 0

for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)