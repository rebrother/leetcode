class Solution:
    def judgeCircle(self, moves: str) -> bool:
        li = list(moves)
        LR = 0
        UD = 0
        
        for i in li:
            if i == 'R':
                LR += 1
            elif i == 'L':
                LR -= 1
            elif i == 'U':
                UD += 1
            elif i == 'D':
                UD -= 1
        
        if LR == 0 and UD == 0:
            return True
        else:
            return False
        