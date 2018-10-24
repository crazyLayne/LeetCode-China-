class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        for line in grid:
            line.append(-1)
        grid.append([-1]*(N+1))
        grid[-1][-2] = 0
        grid[-2][-1] = 0
        # 从左上到右下再从右下到左上，可以看做是两个人同时从左上到右下，两个人同步走，同一个方格的樱桃只能捡一次
        # 为了方便编写代码，我们选择从右下角走到左上角
        # dp[x1,y1,x2](x1,y1)表示第一个人坐标，(x2,y2)表示第二个人坐标，由于两个人同步在走，y2=x1+y1-x2
        # dp[x1,y1,x2]表示两个人从g[0][0]达到各自坐标所能获得的最大樱桃数目
        # dp[x1][y1] = max(dp[x1+1][y1], dp[x1][y1+1]) dp[x2][y2]类似
        # dp[x1,y1,x2] = g[x1][y1] + g[x2][y2] + dp[x1][y1] + dp[x2][y2]  
        # 首先g(x1,y1)!=-1 and g(x2,y2)!=-1; 其次 if x1==x2 (y1必定等于y2) 表示达到同一个点，g[x][y]只能算一次
        dp = [[[0]*(N+1) for i in range(N+1)] for j in range(N+1)]
        for x1 in range(N-1, -1, -1):
            for y1 in range(N-1, -1, -1):
                for x2 in range(x1+y1, -1, -1):
                    y2 = x1 + y1 - x2
                    if x2>=0 and x2<N and y2>=0 and y2<N and grid[x1][y1]!=-1 and grid[x2][y2]!=-1:
                        # 两个人都有两种走法，总共有四种走法
                        if not (grid[x1+1][y1]!=-1 or grid[x1][y1+1]!=-1):  #第一个人无法到达,考虑连续性，所以改写grid[x][y]的值 
                            grid[x1][y1]=-1
                        elif not (grid[x2+1][y2]!=-1 or grid[x2][y2+1]!=-1):  #第二个人无法到达
                            grid[x2][y2]=-1
                        else:
                            dp[x1][y1][x2] = max(dp[x1+1][y1][x2+1], dp[x1+1][y1][x2], dp[x1][y1+1][x2+1], dp[x1][y1+1][x2])
                            dp[x1][y1][x2] += grid[x1][y1] + grid[x2][y2] if x1!=x2 else grid[x1][y1]
        return dp[0][0][0]

grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# grid = [[0,1,1,0,0],[1,1,1,1,0],[-1,1,1,1,-1],[0,1,1,1,0],[1,0,-1,0,0]]
s = Solution()
print(s.cherryPickup(grid))                 
                