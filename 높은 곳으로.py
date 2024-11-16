t = int(input())  # 테스트 케이스의 수
for tc in range(1, t + 1):
    n, p = map(int, input().split())  # n: 선택 횟수, p: 폭탄이 설치된 층
    start = 0  # 엘리베이터의 초기 위치

    for i in range(1, n + 1):  # 선택 횟수만큼 반복
        start += i  # 현재 선택에서 i층을 올림
        if start == p:  # 만약 start가 폭탄이 설치된 층이라면
            start -= 1  # 폭탄을 피하기 위해 1층 내려줌

    print(start)  # 가장 높은 층을 출력
