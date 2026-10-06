class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        print(sorted_nums)
        max_consec = 1
        curr_consec = 1
        for i in range(len(nums)-1):
            if sorted_nums[i+1] == sorted_nums[i]:
                continue
            if (sorted_nums[i+1] - 1) ==  sorted_nums[i]:
                curr_consec += 1
            else:
                print(sorted_nums[i])
                
                if curr_consec >= max_consec:
                    max_consec = curr_consec
                curr_consec = 1
        if curr_consec >= max_consec:
                    max_consec = curr_consec
        return max_consec