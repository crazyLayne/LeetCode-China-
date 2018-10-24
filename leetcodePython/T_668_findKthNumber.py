class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def LEX(m, n, x, k):       #返回m*n乘法表中不大于x的个数
            count = 0
            #总共m行，每一行等于i*j，最小值为i*1，最大值为i*n，这一行中比x小的元素为x//i个
            for i in range(1,min(m+1, x+1)):
                count += min(n, x//i)
                if count>=k:return count
            return count

        # 对于m*n的乘法表，总共有m*n个整数，最小的为1，最大的为m*n，内部存在重复整数，数值在【1，m*n】之间
        # 二分查找【1，m*n】之间的一个数x，sum(y,y<=x)==k,x就是第k个数字了
        l, r = 1, m*n
        while l<r:
            x = (l+r)//2
            if LEX(m, n, x, k)>=k:
                r = x
            else:
                l = x+1
        return l
    
    def findKthNumber2(self, m, n, k):      #上面方法重写
        l,r = 1, m*n
        while l<r:
            x = (l+r)//2
            count = 0
            for i in range(1, m+1):
                count += min(n, x//i)
                if count>=k: break
            if count>=k:
                r = x
            else:
                l = x+1
        return x
