class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        # pivot = 0
        while low<high:
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        pivot = low
        print(pivot)

        if target == nums[pivot]:
            return pivot
        
        if target <= nums[-1]:
            low,high = pivot,len(nums)-1
        else:
            low,high = 0,pivot

        while low <= high:
            # Prevents potential integer overflow in other languages
            mid = low + (high - low) // 2 
            
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Ignore left half
            else:
                high = mid - 1  # Ignore right half
                
        return -1 



        return -1
                