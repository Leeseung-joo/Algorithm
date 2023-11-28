
n, k = map(int,input().split())

def nk(n,k):
	if n //k == 1 and n % k == 0:
		return "yes"
	elif k == 1:
		return "no"
	elif n%k == 0:
			return nk(n//k,k)
	else:
		return "no"
		
result = nk(n,k)
print(result)
