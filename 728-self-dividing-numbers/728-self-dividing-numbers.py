class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            tmp = list(str(i))
            tmp = map(int, tmp)
            tmp = list(tmp)
            if 0 in tmp:
                continue
            result.append(i)
            for j in tmp:
                if i % j != 0:
                    result.remove(i)
                    break
        return result