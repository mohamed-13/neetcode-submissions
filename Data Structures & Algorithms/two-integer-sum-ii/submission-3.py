class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx,i in enumerate(numbers):
           new_target = target - i
           if new_target in numbers:
            return [idx+1 , numbers.index(new_target)+1]