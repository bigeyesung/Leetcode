#https://www.itread01.com/content/1541966776.html

#https://medium.com/@syedtousifahmed/fibonacci-iterative-vs-recursive-5182d7783055#:~:text=Space%20Complexity%3A&text=Hence%20it's%20space%20complexity%20is,the%20implicit%20function%20call%20stack.

class Solution:
    def fib(self, n: int) -> int:
        #time:O(2**n):each time: we call same function twice
        #space:O(1)
        # def calculate(n):
        #     if n<=1:
        #         return n
        #     else:
        #         return calculate(n-1)+calculate(n-2)
        # ret=calculate(n)
        # return ret
        
        # #time:O(n)
        # #space:O(n)
        # if n<=1:
        #     return n
        # arr = [0]*(n+1)
        # arr[0],arr[1]=0,1
        # for ind in range(2,n+1):
        #     arr[ind]=arr[ind-1]+arr[ind-2]
        # return arr[n]
    
    
        #time:O(n)
        #space:O(1)
        if n<=1:
            return n
        cur=2
        first=0
        second=1
        for ind in range(2,n+1):
            cur=first+second
            first=second
            second=cur
        return cur

