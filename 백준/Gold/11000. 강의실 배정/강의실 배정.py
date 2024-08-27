import heapq

# 입력 받기
n = int(input())
time = []

for _ in range(n):
    st, et = tuple(map(int, input().split()))
    time.append([st, et])    # [강의 종료 시간, 강의 시작 시간]으로 저장

# 정렬하기
time.sort()
heap = []
heapq.heappush(heap, time[0][1])

for i in range(1, len(time)):
    # print(heap)
    if time[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])
    else:
        heapq.heappush(heap, time[i][1])

print(len(heap))
