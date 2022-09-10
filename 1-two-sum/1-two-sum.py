class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            search = target - nums[i]
            nums2 = nums[i+1:]
            if search in nums2:
                return [i, nums.index(search, i+1)]