class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.row = n_rows
        self.col = n_cols
        self.count = 0
        

    def flip(self):
        """
        :rtype: List[int]
        """
        return [self.count/self.col, self.count%self.col]
        self.count += 1
        

    def reset(self):
        """
        :rtype: void
        """
        self.count = 0
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()