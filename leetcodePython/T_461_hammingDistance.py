class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x^y
        res = 0
        while z!=0:
            if z%2==1: res+=1
            z//=2
        return res
    def hammingDistance2(self, x, y):
        return (bin(x^y)).count('1')