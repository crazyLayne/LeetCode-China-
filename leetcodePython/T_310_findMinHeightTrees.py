import math
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        map = {}    # int:List[int] 点与它相连的的点
        dis = [ [0] * n for _ in range(n)]      #各个点之间的距离，除了对角线的0表示无法到达
        for pp in edges:
            [p1, p2] = pp
            dis[p1][p2] = 1
            dis[p2][p1] = 1
            if p1 in map:
                p1s = map[p1]
                p1s.append(p2)
                map[p1] = p1s
            else:
                map[p1] = [p2]
            if p2 in map:
                p2s = map[p2]
                p2s.append(p1)
                map[p2] = p2s
            else:
                map[p2]=[p1]
        # print(map)
        for k in range(n):
            for i in range(n):
                for j in range(i+1,n):
                    if k in map[i] and k in map[j]:
                        if dis[i][j]==0:
                            dis[i][j] = dis[i][k] + dis[k][j]
                            dis[j][i] = dis[i][j]
                            pis = map[i]
                            pjs = map[j]
                            pis.append(j)
                            pjs.append(i)
                            map[i] = pis
                            map[j] = pjs
                        elif dis[i][j]>dis[i][k]+dis[k][j]:
                            dis[i][j] = dis[i][k]+dis[k][j]
                            dis[j][i] = dis[i][j]
        print(dis)
        maxLen = max(max(dis))
        edg = math.ceil(maxLen/2)
        res = set(range(n))
        print(maxLen, edg, res)
        for i in range(n):
            for j in range(n):
                if dis[i][j] > edg:
                    if i in res: res.remove(i)
                    if j in res: res.remove(j)
                    break
        return list(res)
        


slt = Solution()
# n = 4
# edges = [[1, 0], [1, 2], [1, 3]]
n=6
edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]
print(slt.findMinHeightTrees(n, edges))
