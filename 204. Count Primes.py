class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        size =int(n ** 0.5) + 1
        for i in range(2, size):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

if __name__ == "__main__":
    arr=[1,2,3,4]
    arr[1:4:2] = [-1]*2
    sol=Solution()
    ret=sol.countPrimes(10)
    print(ret)