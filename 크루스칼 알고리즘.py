def find_parent(parent,x): #parent는 부모테이블임(리스트)
    if parent[x] != x: #부모노드가 자기자신이 아니면
        parent[x] = find_parent(parent,parent[x]) #재귀를 이용해 x의 parent가 루트가되도록 설정
    return parent[x]

def union_parent(parent,a,b,):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    v,e = map(int,input().split())
    parent = [0] * (v+1)
    
    edges = []
    result = 0
    
    for i in range(1,v+1):
        parent[i] = i
        
    for _ in range(e):
        a,b,cost = map(int,input().split())
        edges.append((cost,a,b)) #비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
        
    edges.sort()
    
    for edge in edges:
        cost,a,b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
    print(result)
            
        
    