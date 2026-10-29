class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        low,high = 0,len(nums)-1
        
        while low < high:
            print(nums[low:high+1])
            mid = low + (high-low)//2
            print(low,mid,high)
            if nums[mid] > nums[high]:
                low = mid+1
            elif nums[mid]<nums[high]:
                high = mid

        return nums[low]