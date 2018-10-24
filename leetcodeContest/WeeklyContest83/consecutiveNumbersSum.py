class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 如果N是奇数，必须（奇数个连续数字，且中间必须为奇数）或者（偶数个连续数字，且不能为4的倍数）
        # 如果N是偶数，必须（奇数个连续数字，且中间必须是偶数）或者（偶数个连续数字，且必须是4的倍数）
        i, count = 1, 0
        if N%2==0:          # N是偶数
            while True:
                if N/i < i/2: break
                if i%2==0:      # i是偶数
                    if i%4==0 and N%i!=0 and N*2%i==0:     # i必须是4的倍数且N/i恰好在中间
                        count+=1
                else:           # i是奇数
                    if N%i==0 and N/i%2==0:     # N/i是整数且偶数
                        count+=1               
                i+=1
        else:               # N是奇数
            while True:
                if N/i < i/2: break
                if i%2==0:      # i是偶数
                    if i%4!=0 and N%i!=0 and N*2%i==0:     # i不能是4的倍数且N/i恰好在中间
                        count+=1
                else:           # i是奇数
                    if N%i==0 and N/i%2!=0:     # N/i是整数且奇数
                        count+=1
                i+=1
        return count
s = Solution()
print(s.consecutiveNumbersSum(8 ))


