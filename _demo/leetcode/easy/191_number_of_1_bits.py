class Solution:
    def hammingWeight(self, n: int) -> int:
        # Not using bin() since I think it is not how this question is designed.
        counts = 0
        for i in range(31, -1, -1):
            if n >= 2**i:
                counts = counts + 1
            n = n - 2**i
        # Another tricks I learn is using bit tricks with n >> 1
        return counts