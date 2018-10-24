class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        # 用dp[i][j][k]来描述boxes的状态，表示b[i]~b[j]后面接着K个b[j]元素的最大得分
        # dp[i][j][k] = dp[i][j-1][0] + (k+1)^2     case1: 先把后面的分给拿了
        # dp[i][j][k] = max(dp[i][p][k+1] + dp[p+1][j-1][0])    case2: 在b[i]~b[j]之间寻找b[p]=b[j],继续攒积分
        self.boxes = boxes
        self.n = len(boxes)
        # self.dp = [[[0]*len(boxes) for i in range(len(boxes))] for j in range(len(boxes))]
        self.dict = {}      #由于dp[i][j][k]中存在许多未访问的节点，即dp很稀疏，我们用key = self.n*(self.n*i+j)+k的字典来代替dp
        return self.DFS(0,len(boxes)-1, 0)

    def DFS(self, i, j, k):
        if i==j: return (1+k)**2        # 只有一个元素
        if i>j: return 0                # 非法范围
        while j>i and self.boxes[j-1]==self.boxes[j]:       #合并最右端的相同元素
            j -= 1
            k += 1
        key = self.n*(self.n*i+j)+k
        if key in self.dict: return self.dict[key]     #已经计算过了
        case1 = self.DFS(i, j-1, 0) + (k+1)**2
        case2 = 0
        for p in range(i, j):
            if self.boxes[p] == self.boxes[j]:
                case2 = max(case2, self.DFS(i, p, k+1) + self.DFS(p+1, j-1, 0))
        self.dict[key] = max(case1, case2)
        return self.dict[key]


boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
# boxes = [1, 2, 1, 3, 1]
s = Solution()
print(s.removeBoxes(boxes))