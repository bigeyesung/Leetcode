class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n!=1 and n not in cycle:
            cycle.add(n)
            n= sum(int(i)**2 for i in str(n))
        return n==1
    
        # seen = set()
        # def compute_squares(number):
        #     return sum([int(char)**2 for char in str(number)])
        # res = n
        # while True:
        #     res = compute_squares(res)
        #     if res == 1:
        #         return True
        #     if res in seen:
        #         return False
        #     seen.add(res)
if __name__ == "__main__":
    print(len("dog cat"))
    sol = Solution()
    ret = sol.isHappy(2)