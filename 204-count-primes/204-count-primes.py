class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        if n>1:
            primes=[True for t in range(n)]
            p=2
            while(p*p<n):
                if primes[p]:
                    for m in range(p ** 2,n,p):
                        primes[m]=False
                p+=1
            for c in primes:
                if c:
                    count+=1
            return count-2

        else:
            return count