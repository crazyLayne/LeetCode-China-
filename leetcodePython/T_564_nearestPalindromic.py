class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if n=="0":return "1"
        if len(n)==1:return str(int(n)-1)
        N = int(n)
        n = list(n)
        n1 = 10**len(n)+1           #比n多一位，形如11，101，1001，。。。
        n2 = int("9"*(len(n)-1))    #比n少一位，形如9，99，999，。。。
        for i in range(len(n)//2):
            n[len(n)-1-i] = n[i]
        n3 = int(''.join(n))        #通过改动低位的值，将n构造成回文
        if n3==N:                   #n本来就是个回文，不考虑自身
            n3=0
        n4,n5=0,0
        if n[len(n)//2]<'9':        #将n(已经是回文了)的中间元素（奇数一个偶数两个）加一或减一
            newn = n.copy()
            newn[len(n)//2] = str(int(newn[len(n)//2])+1)
            if len(n)%2==0: newn[len(n)//2-1] = newn[len(n)//2]
            n4 = int(''.join(newn))
        if n[len(n)//2]>'0':
            newn = n.copy()
            newn[len(n)//2] = str(int(newn[len(n)//2])-1)
            if len(n)%2==0: newn[len(n)//2-1] = newn[len(n)//2]
            n5 = int(''.join(newn))
        return str(self.closed(N,n1,n2,n3,n4,n5))
    def closed(self,N,n1,n2,n3,n4,n5):      #从这几种可能中选择最接近的
        res = n2
        if abs(N-n5)<abs(N-res):res = n5
        if abs(N-n3)<abs(N-res):res = n3
        if abs(N-n4)<abs(N-res):res = n4
        if abs(N-n1)<abs(N-res):res = n1
        return res
            

