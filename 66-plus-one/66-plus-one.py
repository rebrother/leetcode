class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''.join((map(str, digits)))
        result = str(int(result) + 1)
        result = map(int, result)
        result = list(result)
        return result