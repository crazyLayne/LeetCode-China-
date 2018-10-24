class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 两种错误，奇数位置放偶数，偶数位置放奇数，交换这两种错误
        err1 = []
        err2 = []
        for i,n in enumerate(A):
            if i%2==0 and n%2!=0: err1.append(i)
            elif i%2!=0 and n%2==0: err2.append(i)
        for i in range(len(err1)):
            A[err1[i]], A[err2[i]] = A[err2[i]], A[err1[i]]
        return A
