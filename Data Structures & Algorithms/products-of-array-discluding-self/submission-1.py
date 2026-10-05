class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for idx,i in enumerate(nums):
            inter_res = 1
            for idx1,j in enumerate(nums):
                if idx!=idx1:
                    inter_res *= j
            res.append(inter_res)

        return res