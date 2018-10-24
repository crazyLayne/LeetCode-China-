# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        maxc = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                count = 0
                ps = set()
                for k in range(j+1, n):
                    x, y = points[k].x, points[k].y
                    if (x,y) not in ps:
                        if self.isOneLine(points[i],points[j],points[k]):count+=1
                        ps.add((x,y))
                maxc = max(maxc, count)
        return maxc
        
    def isOneLine(self, p1, p2, p3):
        return p1.x*(p2.y-p3.y) + p2.x*(p3.y-p1.y) + p3.x*(p1.y-p2.y) == 0
        
ps = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]
ps = [(1,2),(1,2)]
print(len(ps))
ps = set(ps)
print(ps)
print(len(ps))