class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        unvisit = set(list(range(len(M))))
        count = 0
        while len(unvisit)>0:
            count += 1
            p = unvisit.pop()
            # DFS遍历p的所有节点
            self.DFS(M, unvisit, p)
        return count
    
    def DFS(self, M, unvisit, cur):
        for i in range(len(M)):
            if M[cur][i]==1 and i in unvisit:
                unvisit.remove(i)
                self.DFS(M, unvisit, i)
        
M = [[1,1,0],[1,1,0],[0,0,1]]
s = Solution()
print(s.findCircleNum(M))