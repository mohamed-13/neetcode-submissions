class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create map mapping num to index
        m = dict()

        # iterate nums
        for i, num in enumerate(nums):
            # for each iteration check if target-nums[i] in map. if yes, return both indexes
            if target - num in m:
                return [m[target - num], i]
            
            m[num] = i

        return None