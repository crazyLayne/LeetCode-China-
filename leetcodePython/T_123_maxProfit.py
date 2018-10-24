class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0: return 0
        p1 = [0]*len(prices)
        p2 = [0]*len(prices)
        p3 = [0]*len(prices)
        p4 = [0]*len(prices)
        for i in range(len(prices)):
            p1[i] = -prices[i]
            p2[i] = max(p1[:i])+prices[i] if i>0 else 0
            p3[i] = max(p2[:i])-prices[i] if i>0 else -prices[i]
            p4[i] = max(p3[:i])+prices[i] if i>0 else 0
        return max(p4)
    def maxProfit3(self, prices):       #从maxProfit1修改得到，p1,p2,p3,p4都没必要记录整个序列，只需要记录当前最大就可以了
        if len(prices)==0: return 0
        p1, p3 = -10000, -10000
        p2, p4 = 0, 0
        for p in prices:
            p1 = max(p1,-p)
            p2 = max(p2, p1+p)
            p3 = max(p3, p2-p)
            p4 = max(p4, p3+p)
        return p4
        
    def maxProfit2(self, prices):
        if len(prices)==0: return 0
        p = []
        for i in range(1,len(prices)-1):
            if prices[i]<=prices[i-1] and prices[i]<prices[i+1]:
                p.append(self.maxP(prices, 0, i) + self.maxP(prices, i, len(prices)))
        if len(p)>0: return max(p)
        else: return self.maxP(prices, 0, len(prices))

    def maxP(self, prices, L, R):
        maxp = 0
        minv = prices[L]
        for i in range(L, R):
            minv = min(minv, prices[i])
            maxp = max(maxp, prices[i]-minv)
        return maxp

prices = [1, 2, 3, 4, 5]
s = Solution()
print(s.maxProfit2(prices))
print(s.maxP(prices, 0, len(prices)))
