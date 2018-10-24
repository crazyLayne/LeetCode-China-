class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z==0 or x==z or y==z:return True
        if x==0 or y==0 or z>x+y:return False        
        return z%self.maxCommonDivisor(min(x,y),max(x,y))==0
    def maxCommonDivisor(self, x, y):
        if y%x==0:
            return x
        else:
            rem = y%x
            return self.maxCommonDivisor(min(x,rem), max(x,rem))

x = 104681
y = 104683
z = 54
s = Solution()
print(s.canMeasureWater(x,y,z))