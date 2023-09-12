class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        
        
        
        for currentSum in range(1, target + 1):
            dp[currentSum]=0
               
            for i in nums:
                dp[currentSum]+=dp.get(currentSum-i,0)
            
        return dp[target]
