import math
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<=3: return max(2, N)
        if N%2==0: N+=1
        while self.isPal(N)==False or self.isPrime(N)==False:
            if len(str(N))%2 == 0 and N != 11: #判断是否是除11之外的偶数位数字
                N = int(math.pow(10,len(str(N))))+1;#直接跳过偶数位数字
            else: N += 2
        return N
    
    
    def isPal(self, num):
        s = str(num)
        ln = len(s)
        for i in range(ln//2):
            if s[i]!=s[ln-1-i]:return False
        return True
    def isPrime(self, num):
        if num<=3:return True
        for i in range(2, int(num**0.5)+1):
            if num%i==0: return False
        return True