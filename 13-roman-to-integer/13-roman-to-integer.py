class Solution:
    def romanToInt(self, s:str):
        sum = 0
        Sym = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        s = list(s)
        for i in s:
            sum += Sym[i]
        for i in range(len(s)-1):
            if s[i] == 'I' and (s[i+1] == "V" or s[i+1] == "X"):
                sum-=2
            elif s[i] == 'X' and (s[i+1] == "L" or s[i+1] == "C"):
                sum-=20
            elif s[i] == 'C' and (s[i+1] == "D" or s[i+1] == "M"):
                sum-=200
        return sum
