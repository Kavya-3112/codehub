from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        t=set(list(permutations(list(nums))))
        return t
