class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)
        if k==len(num):return '0'
        i=0
        j=0
        while i<k:
            #每一轮从前往后寻找一个相邻递减元素对，删除前者
            while j<len(num)-1 and num[j]<=num[j+1]:j+=1
            del num[j]
            if j==0 and num[j]=='0':  #删除前导零
                while j<len(num) and j<num[j]=='0':
                    del num[j]
            elif j>0: j-=1  #向前挪一位
            i+=1
        return ''.join(num) if len(num)>0 else '0'

# s = Solution()
# num = list("10200")
# k = 1
# print(s.removeKdigits(num, k))