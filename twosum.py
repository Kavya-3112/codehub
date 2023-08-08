
def twoSum(self, nums, target):

    for i in range(len(nums)):
        for k in range(i+1,len(nums)):
            cnt=nums[i]+nums[k]
            if cnt==target:
                return [i,k]
