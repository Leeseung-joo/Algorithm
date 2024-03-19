#2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a): #a는 key임
    n = len(a) #행길이
    m = len(a[0]) #열길이
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True



def solution(key,lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)] #자물쇠의 크기를 기존의 3배로 변환
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j] 
#4가지 방향에 대해서 확인          
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) #열쇠 회전
        for x in range(1,2*n):
            for y in range(1,2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]  #자물쇠에 열쇠를 끼워넣기
                if check(new_lock) == True:
                    return True #열쇠가자물쇠에 잘 들어맞는지 검사
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j] #자물쇠에서 열쇠를 다시 빼기
    return False
        
        
    
    
    