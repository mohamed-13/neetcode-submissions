class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) -1

        while (left < right):
            
            inter_sum = numbers[left] + numbers[right]

            if inter_sum == target:
                return [left+1,right+1]

            if inter_sum < target:
                left += 1
            else:
                right -=1
        