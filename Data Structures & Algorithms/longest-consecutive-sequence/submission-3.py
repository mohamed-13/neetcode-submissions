class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        validator = []
        nums = sorted(set(nums))
        print(nums)
        pointer_1 = 0
        pointer_2 = 1
        counter = 1
        if len(nums) == 0:
            return 0
        while pointer_2 < len(nums):
            print(nums[pointer_1] , nums[pointer_2])
            if (nums[pointer_2] - nums[pointer_1]) == 1:
                counter+= 1
            else:
                validator.append(counter)
                counter = 1
            
            pointer_1 += 1
            pointer_2 += 1
        validator.append(counter)
        return max(validator)