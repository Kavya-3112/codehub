class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        t=[]
        for i ,m in enumerate (mat):
            c=(sum(m),i)
            t.append(c)
        t.sort()
        return [i[1] for i in t[:k]] 
