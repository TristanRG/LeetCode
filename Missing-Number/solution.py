class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0
        
        elif nums[0] != 0:
            return 0
        
        elif len(nums) == 1:
            return nums[0] + 1

        for i in range(len(nums) -1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i + 1] - 1
            
        return nums[-1] + 1
        