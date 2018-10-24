class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:return len(s)
        dp = [[0]*len(s) for _ in range(len(s))]    #dp[i][j]表示s[i:j+1]的最长回文子序列
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i==j: dp[i][j]=1
                else:
                    if s[i]==s[j]: dp[i][j] = dp[i+1][j-1]+2 if i+1<=j-1 else 2
                    else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]