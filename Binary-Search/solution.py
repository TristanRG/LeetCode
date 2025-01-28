class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return nums.index(target)
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        