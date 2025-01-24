class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        
        array = []
        start = nums[0]
        
        if len(nums) == 1:
            array.append(f"{start}")
            return array

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    array.append(str(start))
                
                else:
                    array.append(f"{start}->{nums[i]}")
                start = nums[i + 1]
            

        if start == nums[-1]:
            array.append(str(start))
        else:
            array.append(f"{start}->{nums[-1]}")
            
        return array