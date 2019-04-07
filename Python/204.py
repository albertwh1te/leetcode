# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n: int) -> int:
        # Solution
        # http://www.cnblogs.com/grandyang/p/4462810.html
        if n <= 2:
            return 0
        prime = [1 for i in range(n+1)]
        result = 0
        for i in range(2, n):
            if prime[i]:
                result += 1
                for j in range(n//i+1):
                    prime[j*i] = 0
        return result


if __name__ == "__main__":
    r = Solution().countPrimes(2)
    print(r)

    r = Solution().countPrimes(10)
    print(r)
