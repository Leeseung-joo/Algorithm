n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
total = 0
k = 0
for i in list1:
    total += i * (len(list1) - k)
    k += 1
print(total)


# for x in range(1, n+1):
#     answer += sum(peoples[0:x])  # 리스트의 0번째 수부터 x번째 수까지를 더해줍니다.
# print(answer)  # 정