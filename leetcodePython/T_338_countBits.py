class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num==0:return [0]
        if num==1:return [0,1]
        dp = [0]*(num+1)
        dp[0], dp[1] = 0, 1
        divisor = 1
        for i in range(2,num+1):
            if i%divisor==0: divisor*=2
            dp[i] = dp[i%divisor]+1
        return dp
