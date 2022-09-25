class Solution:
    def countAsterisks(self, s: str) -> int:
        bar_count = 0
        count = 0
        for i in s:
            if i == '|':
                bar_count += 1
            if bar_count % 2 == 0 and i == '*':
                count += 1
        return count