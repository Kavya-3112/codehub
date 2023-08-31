def findMaxAverage(self, nums: List[int], k: int) -> float:
        crt,maxi=0,0
        for i in range(len(nums)-k):
            crt+=nums[i+k]-nums[i]
            maxi=max(crt,maxi)
        l=(sum(nums[:k])+maxi)/k
        return l
