L = int(input())
M = 1234567891
r = 31
str = input()
answer = 0
for i in range(len(str)):
    num = ord(str[i]) - 96
    answer += num * (r**i)
print(answer % M)
