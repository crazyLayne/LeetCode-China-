class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        if n >= 10:
            n = 10
        ans = 91
        j = 8
        temp = 81
        i = 3
        while i <= n:
            temp = temp * j
            ans = ans + temp
            j = j - 1
            i = i + 1
        return ans