class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_capacity = 0
        l,r = 0,len(heights)-1

        while l<r:
            capacity = min(heights[l],heights[r]) * (r-l)

            if  capacity > max_capacity:
                max_capacity = capacity
            
            if heights[l]>heights[r]:
                r -=1
            else:
                l +=1

        return max_capacity