input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord - >10진수 유니코드로 바꾼 다음에, a에 해당하는 유니코드값을 빼주고 1을 더해서 정수로 만들어줌

steps = [(-2,-1),(-1,-2),(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)

