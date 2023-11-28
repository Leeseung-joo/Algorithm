M,e,d,n = map(int, input().split())
def exp1(M,e,n):
	if e == 1:
		return M % n
	elif (e % 2) == 0:
		return ((exp1(M, (e/2), n)**2) % n)
	else:
		return (M*exp1(M, e-1, n)) % n
k = exp1(M,e,n)
print(int(k))
w = exp1(k,d,n)
print(int(w))
	
