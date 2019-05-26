
#recursive
class Solution:
    def fib(self, N):

        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

        
#iterative        
class Solution:
    def fib(self, N):

        if N == 0:
            return 0
        elif N == 1:
            return 1
        pre1 = 1
        pre2 = 0
        for i in range(2, N+1):
            res = pre1 + pre2
            pre2 = pre1
            pre1 = res
        return res
