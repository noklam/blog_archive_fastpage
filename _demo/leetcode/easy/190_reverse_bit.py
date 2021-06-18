"""
Almost same as numbers of 1 bits, except a trick to use sum 2**(31-i) since we know there are 32 bits.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range (32,0, -1):
            i = i -1
            if n >= 2**i:
                n = n - 2**i
                ans = ans + 2**(31-i)
        return ans