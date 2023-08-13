class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        k=len(nums)
        return nums[k//2]
