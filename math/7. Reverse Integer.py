class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        rev = 0
        x = abs(x)
        while x:
            rev = rev*10 + x%10
            x = x // 10
        return rev*sign if rev <= 2**31-1 else 0
