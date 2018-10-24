class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves)%2!=0: return False
        cup = cdown = cleft = cright = 0
        for i in range(len(moves)):
            c = moves[i]
            if c=='U': cup+=1
            elif c=='D': cdown+=1
            elif c=='L': cleft+=1
            else: cright+=1
            if abs(cleft-cright)+abs(cup-cdown)> len(moves)-i-1: return False
        return cup==cdown and cleft==cright
    def judgeCircle2(self, moves):
        if len(moves)%2!=0: return False
        cup = moves.count('U')
        cdown = moves.count('D')
        cleft = moves.count('L')
        cright = moves.count('R')
        return cup==cdown and cleft==cright