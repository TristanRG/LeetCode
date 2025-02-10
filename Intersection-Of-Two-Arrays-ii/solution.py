class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1)
        intersection = []
        for x in nums2:
            if cnt[x] > 0:
                intersection.append(x)
                cnt[x] -= 1
        return intersection
        