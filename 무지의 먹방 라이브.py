import heapq


#food times는 각 음식을 먹는데 필요한 시간이 담긴 배열, 방송이 중단된 시간
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))
    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간간
    length = len(food_times) #남은 음식의 개수
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1 #다 먹은 음식 제외
        previous = now #이전 음식 시간 재설정
    #남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q,key = lambda x: x[1]) #음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length[1]]
                