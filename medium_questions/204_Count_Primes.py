class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True]*n
        
        for i in range(2, math.ceil(n/2)):
            if primes[i]:
                for j in range(i, ceil(len(primes)/i)):
                    primes[i*j] = False
        primeCount = 0
        for i in range(2, len(primes)):
            if primes[i]:
                primeCount+=1
        return primeCount
        