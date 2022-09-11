import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        past_li = []
        str_n = str(n)
        while 1:
            li = list(str_n)
            arr_n = np.array(list(map(int, li)))
            str_n = str(sum(arr_n**2))
            if str_n == '1':
                break
            elif str_n in past_li:
                return False
            past_li.append(str_n)
        return True