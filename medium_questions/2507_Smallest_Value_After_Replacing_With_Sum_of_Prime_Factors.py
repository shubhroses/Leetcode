class Solution:
    def smallestValue(self, n: int) -> int:
        """
        Get the primes of n
            1. Compute all primes from 2 to 10^5
        
        replace n with sum of primes
        
        Continue until n is a prime number
        """
        
        def isPrime(num):
            if num <= 1:
                return False
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    return False
            return True
        
        def getPrimeFactors(x):
            res = []
            while x % 2 == 0:
                res.append(2)
                x = x / 2
            
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                while x % i == 0:
                    res.append(i)
                    x = x/i
            if x > 2:
                res.append(x)
            return res
        
        while not isPrime(int(n)):
            old = n
            n = sum(getPrimeFactors(n))
            if n == old:
                break
        return int(n)