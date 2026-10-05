class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx,i in enumerate(numbers):
            diff = target - i
            if diff in seen:
                return [seen[diff]+1,idx+1]
            seen[i] = idx
