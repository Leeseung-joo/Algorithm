n = int(input())
list1 = []
for i in range(n):
    a,b= map(str,input().split())
    list1.append([int(a),b])
list2 = sorted(list1, key = lambda x:x[0])
for j in range(n):
    print(list2[j][0], list2[j][1])