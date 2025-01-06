class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set()
        for num in nums:
            if num not in n:
                n.add(num)

            else:
                return True

        return False
