class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        k="".join(str(i) for i in digits)
        k=str(int(k)+c)
        return [int(i) for i in k]
