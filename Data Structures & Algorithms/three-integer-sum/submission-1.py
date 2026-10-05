class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_res = []
        nums.sort()
        for idx,number in enumerate(nums):

            if idx>0 and number == nums[idx-1]:
                continue
            l,r = idx+1 , len(nums)-1

            while l<r:
                add = number+nums[l]+nums[r]
                if add == 0:
                    final_res.append([number,nums[l],nums[r]])
                    l+=1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif add > 0:
                    r -= 1
                else:
                    l += 1

        return final_res 