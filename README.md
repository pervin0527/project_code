# 코딩테스트 대비
- Windows
- Python3

# 피드백

1. 입력 값 받을 때  
  
        # input()보다 빠름.
        sys.stdin = open()

        # 입력 값 1개를 int형으로 입력 받을 때
        a = int(inut())

        # 입력 값 n개를 int 형으로 입력 받을 때
        a, b = map(int, input().split())

        # list 타입으로 입력 받을 때
        a = list(map(int, input().split()))

2. for ~ else 문.

        # for 문 중간에 break 등으로 끊기지 않고, 끝까지 수행 되었을 때 동작하는 코드.

        date = [2, 4, 5, 11, 3]
        for i in data:
            if i > 10:
                break

            else:
                print('10보다 큰 수 없음')

3. sort() - 오름차순 정렬

        a = list(map(int, input().split()))
        a.sort()

4. list 슬라이싱

        # end 지점은 원하는 것보다 1 작은 인덱스 값이므로 +1 해줘야 원하는 범위까지 지정 가능.
        # https://wikidocs.net/2849
        a = list(map(int, input().split()))
        a = a[start:end+1]
