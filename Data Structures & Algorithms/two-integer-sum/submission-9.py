class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dup_dict = {}
        for i in nums:
            if i in dup_dict:
                dup_dict[i] +=1
            else:
                dup_dict[i] = 1 
        for idx,i in enumerate(nums):
            pair = target - i
            
            if pair in nums:
                if idx  == nums.index(pair):
                    if dup_dict[pair] > 1:
                        return [nums.index(i),nums.index(pair,idx+1)]
                    else:
                        continue
                return [nums.index(i),nums.index(pair)]