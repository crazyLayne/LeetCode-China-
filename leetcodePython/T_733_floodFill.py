class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def change(i, j, oriC, nowC, image, m, n):
            if i>=0 and i<m and j>=0 and j<n and image[i][j]==oriC:
                image[i][j]=nowC
                change(i+1,j,oriC,nowC,image,m,n)
                change(i-1,j,oriC,nowC,image,m,n)
                change(i,j+1,oriC,nowC,image,m,n)
                change(i,j-1,oriC,nowC,image,m,n)
        m,n = len(image), len(image[0])
        if image[sr][sc]!=newColor: change(sr,sc,image[sr][sc],newColor,image,m,n)
        return image

image = [[0,0,0],[0,1,1]]
i,j,newColor = 1,1,1
s = Solution()
print(s.floodFill(image,i,j,newColor))