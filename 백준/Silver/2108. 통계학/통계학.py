import sys
n = int(sys.stdin.readline())
list1 = []
dict_li = dict()
for i in range(n):
    list1.append(int((sys.stdin.readline())))
a = round((sum(list1)/n))
if a == -0:
    print(0)
else : 
    print(a)
list1.sort()
print(list1[n//2])
for j in list1:
    if dict_li.get(j) is None:
        dict_li[j] = 1
    else:
        dict_li[j] += 1
mx = max(dict_li.values())
mx_dic = []

for k in dict_li:
    if mx == dict_li[k]:
        mx_dic.append(k)
if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(list1)-min(list1))