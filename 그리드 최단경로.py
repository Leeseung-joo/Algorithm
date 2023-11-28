m,n = map(int,input().split()) #행과 열 입력받음
matrix = []
A = [0]*(m*n)
B = [0]*(m*n)
for _ in range(m):
	row = list(map(int,input().split()))      
	matrix.append(row) #각 자리에 비용이 들어있는 매트릭스 -->이중 리스트임.
p,q = map(int,input().split()) #p,q를 들렸다 가야함.    (1,2)
r = (p-1)*n+q-1 #1차원배열에서의 들렸다 가야할 위치의 인덱스값



def cost(matrix,A,r,p,q,m):
	#matrix[0][4]      #i,j를 가는데 드는 최소 비용구하는 거임
	result = 0
	if n == 1:
		for y in range(m):
			result += matrix[y][0]
		return result
	for k in range(0,n):       #matrix[0][]
		A[k] = matrix[0][k] #리스트에 A[0]~A[n]까지 찻음
	for i in range(n,m*n):
		# if n == 1:
		# 	A[r] = sum(matrix)
		# 	break#8~63까지
		if i % n == 0:
			A[i] = min(A[i-n],A[i-(n-1)]) + matrix[i//n][0] #왼쪽 열
		elif i % n == n-1:             #오른쪽 열
			A[i] = min(A[i-n],A[i-(n+1)]) + matrix[i//n][i%n]
		else:
			A[i] = min(A[i-n], A[i-(n + 1)], A[i-(n - 1)]) + matrix[i//n][i%n]



	 

	for l in range(0,n):
		B[m*n-1-l] = matrix[m-1][n-l-1]
	for j in range(m*n-n-1,-1,-1):
		# if n == 1:
		# 	B[r] = 0
		# 	break
		if j % n == n-1:
			B[j] = min(B[j+n],B[j+(n-1)])+matrix[j//n][j%n]
		elif j % n == 0:
			B[j] = min(B[j+n],B[j+(n+1)])+matrix[j//n][0]
		else:
			B[j] = min(B[j+n],B[j+(n+1)],B[j+(n-1)])+matrix[j//n][j%n]
		if i == r:
			break

	else:		
		result = A[r] + B[r] - matrix[p-1][q-1]
	return result

print(cost(matrix,A,r,p,q,m))
