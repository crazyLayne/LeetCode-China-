class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        # hp[i][j]表示从d[i][j]到达P所需要的最小血量，到达P之后至少需要1点血
        # hp[i][j]可能向下或向右走，我们选择需要血量最小的一条路，即min(hp[i+1][j], hp[i][j+1])
        # 若dungeon[i][j]>0,则说明我们所需要的初始血量可能可以更低，若dungeon[i][j]<0,则说明我们需要更多的初始血量，min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j]
        # 但可能dungeon[i][j]>>0，导致min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j]为负数，我们需要全程保证血量至少为1
        # hp[i][j] = max(1, min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j])
        hp = [[10000000]*(n+1) for _ in range(m+1)] 
        hp[-1][-2]=hp[-2][-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                hp[i][j] = max(1, min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j])
        return hp[0][0]
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
s = Solution()
print(s.calculateMinimumHP(dungeon))