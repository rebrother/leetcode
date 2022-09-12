class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        result = 0
        count 
        for i in nums:
            if i not in dic:
                dic[i] = 1
            elif i in dic:
                dic[i] += 1
        r_dic= dict(map(reversed,dic.items()))
        return r_dic[max(r_dic)]