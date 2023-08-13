from itertools import permutations 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        t=list(permutations(list(nums)))
        return t
