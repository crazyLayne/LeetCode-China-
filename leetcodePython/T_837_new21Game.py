class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K==0 or N>=K+W: return 1   #初始情况满足条件
        res = 0
        p = [0 for _ in range(N+1)]     #p[i]表示数字i出现的概率
        p[0] = 1
        sum = 0.0       #记录可以到达i的前w步概率和
        for i in range(1,N+1):
            # 大于k的从k-1开始，因为大于等于k就不摸牌了
            p[i] = (sum/W+1.0/W) if i<=W else sum/W
            if i>W: sum-=p[i-W]
            if i<K: sum+=p[i]
            if i>=K:
                res += p[i]
        return res
    def new21Game2(self, N, K, W):  #逆向求解，从结果逆推
        d=[0]*(K+max(W,N)+10)
        for i in range(K,N+1):
            d[i]=1
        ms=N-K+1
        for i in range(K-1,-1,-1):
            d[i]=ms/W
            ms+=d[i]-d[i+W]
        return d[0]


N = 21; K = 17; W = 10
s = Solution()
print(s.new21Game(N,K,W))