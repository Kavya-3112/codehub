class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]>nums[k]:
                    nums[i],nums[k]=nums[k],nums[i]
        return nums
