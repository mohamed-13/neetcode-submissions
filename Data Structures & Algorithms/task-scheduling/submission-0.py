class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import Counter,deque
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time +=1
            if maxheap:
                cnt = 1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])
            # if not maxheap:
            #     time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time