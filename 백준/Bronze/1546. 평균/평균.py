N  = int(input())
score = list(map(int,input().split()))
list1 = []
a = max(score)
for i in score:
    list1.append(i/a*100)
print(sum(list1)/len(list1))
