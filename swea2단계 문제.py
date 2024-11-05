t = int(input())  # 테스트 케이스 수 입력
for tc in range(1, t + 1):
    n = int(input())  # 각 테스트 케이스마다 쌍의 수 입력
    print(f"#{tc}")
    result = ""
    for i in range(n):
        char, count = input().split()  # 문자와 반복 횟수 입력
        result += char * int(count)    # 반복된 문자열을 결과 문자열에 추가

    # 결과 문자열을 10개씩 끊어서 출력
    for i in range(0, len(result), 10):
        print(result[i:i+10])
