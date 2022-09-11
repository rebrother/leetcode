class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if str(i) not in dic:
                dic[str(i)] = 0
            dic[str(i)] += 1
        for i in nums:
            if dic[str(i)] == 1:
                return i