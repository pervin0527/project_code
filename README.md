# 코딩테스트 대비
- Windows
- Python3

# 피드백

 - 입력 값 받을 때  
  
        # input()보다 빠름.
        sys.stdin = open()

        # 입력 값 1개를 int형으로 입력 받을 때
        a = int(inut())

- map(함수, data) - 이 data를 함수 처리해라
  
        # 입력 값 n개를 int 형으로 입력 받을 때
        a, b = map(int, input().split())

        # list 타입으로 입력 받을 때
        a = list(map(int, input().split()))

 - for ~ else 문.

        # for 문 중간에 break 등으로 끊기지 않고, 끝까지 수행 되었을 때 동작하는 코드.

        date = [2, 4, 5, 11, 3]
        for i in data:
            if i > 10:
                break

        else:
        print('10보다 큰 수 없음')

 - sort() - 오름차순 정렬

        a = list(map(int, input().split()))
        a.sort()

 - list 슬라이싱

        # end 지점은 원하는 것보다 1 작은 인덱스 값이므로 +1 해줘야 원하는 범위까지 지정 가능.
        # https://wikidocs.net/2849
        a = list(map(int, input().split()))
        a = a[start:end+1]

 - lambda 함수

        # lambda 매개변수 : 함수내용
        # x 값을 인수로 x+2 처리
        test = lambda x : x+2
        print(test)

        def plus_one(x):
          return x+1

        a = [1, 2, 3]
        print(list(map(plus_one, a)))

        print(list(map(lambda x:x+1, a)))