class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words_num = []
        for i in sentences:
            words_num.append(i.count(' ')+1)
        return max(words_num)