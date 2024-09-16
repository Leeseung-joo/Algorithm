alpha = input().lower()
alpha_list = list(set(alpha))
cnt = []

for i in alpha_list:
    count = alpha.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(alpha_list[(cnt.index(max(cnt)))].upper())