class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx,i in enumerate(numbers):
            for j in range(idx+1,len(numbers)):
                if i+numbers[j] == target:
                    return [idx+1 , j+1]