class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1: return len(s)
        dp = [[0]*len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if i==j or (s[i]==s[j] and (i+1==j or dp[i+1][j-1]==1)): 
                    dp[i][j]=1
                    res += 1
                    print(dp)
        return res
    def countSubstrings2(self, s):
        #根据回文中心去判定回文个数
        if len(s)<=1: return len(s)
        res = 0
        for center in range(len(s)*2-1):
            l = center//2
            r = (center+1)//2
            while l>=0 and r<len(s) and s[r]==s[l]:
                res+=1
                l -= 1
                r += 1
        return res

s = 'aaa'
slt = Solution()
print(slt.countSubstrings(s))
print(slt.countSubstrings2(s))
