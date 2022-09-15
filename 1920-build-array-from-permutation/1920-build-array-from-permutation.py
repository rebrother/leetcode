class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        [ans.append(nums[i]) for i in nums]
        return ans