n = int(input())
array = []
for i in range(n):
    input_data = input().split() #split()함수로 인해 공백을 기준으로 리스트로 반환
    array.append((input_data[0],input_data[1]))#튜플로 리스트에 append
array = sorted(array, key = lambda x:x[1]) #디폴트가 오름차순임
for x in array:
    print(x[0],end = ' ')