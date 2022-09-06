class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        
        lis_x = list(ransomNote)
        lis_y = list(magazine)
        
        for i in lis_y:
            ransomNote = ransomNote.replace(i, '', 1)
            
        if ransomNote == '':
            result = True
        return result