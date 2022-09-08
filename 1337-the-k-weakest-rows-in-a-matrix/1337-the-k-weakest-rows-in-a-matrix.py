class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        li = []
        result = []

        for i in range(len(mat)):
            li.append(mat[i].count(1))
            
        comp_li = sorted(li)
        
        for i in range(k):
            result.append(li.index(comp_li[i]))
            li[li.index(comp_li[i])] = 101
            
        return result