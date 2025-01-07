class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possibilities = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in possibilities:
                return [i, possibilities[rest]]

            possibilities[num] = i
        
        return None
