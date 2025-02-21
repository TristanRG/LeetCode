class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            
            elif target > nums[middle]:
                low = middle + 1
            
            else: 
                high = middle - 1
        
        return low 
