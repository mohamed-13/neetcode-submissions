from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        def find_hours(piles,k):
            ct = 0
            if k == 0:
                return False
            for i in piles:
                # print(i,k)
                ct += ceil(i/k)
            if h>= ct:
                return (True)
            else:
                return (False)

        # list_to_iter = [i for i in range(1,k)]

        low, high = 1,k
        final_hr = k
        while low <= high:
            mid = low + (high - low)//2
            verify = find_hours(piles,mid)

            if verify:
                high = mid - 1
                final_hr = mid
            else:
                low = mid + 1

        return final_hr