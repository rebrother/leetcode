class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            result = n
        else:
            result = n * 2
        return result