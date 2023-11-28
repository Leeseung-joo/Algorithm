n = int(input())
c = [0] * max(n + 1, 6)

def stairs(n,c):
	c[1]=1
	c[2]=1
	c[3]=2
	c[4]=4
	c[5]=7
	if n < 6:
		return c[n]

	else:
		for i in range(6,n+1):
			c[i] = c[i-1]+c[i-3]+c[i-4]+c[i-5]
		return c[n]
result = stairs(n,c)
print(result%99999)