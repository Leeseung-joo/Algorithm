n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
# result = sorted(array,reverse = False) 이런경우 오름차순, 아무것도 안적을시 오름차순으로 정렬됨
result = sorted(array,reverse = True)
for i in result:
    print(i, end = ' ')
# print(array) 원래 array는 변하지 않았음
