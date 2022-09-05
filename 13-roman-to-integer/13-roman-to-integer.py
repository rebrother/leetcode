class Solution:
    Sym = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }
    def romanToInt(self, s:str):
        result = 0
        s = list(s)
        for i in s:
            result += self.Sym[i]
        for i in range(len(s)-1):
            if s[i] == 'I' and (s[i+1] == "V" or s[i+1] == "X"):
                result-=2
            elif s[i] == 'X' and (s[i+1] == "L" or s[i+1] == "C"):
                result-=20
            elif s[i] == 'C' and (s[i+1] == "D" or s[i+1] == "M"):
                result-=200
        return result
