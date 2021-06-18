class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, i in enumerate(s):
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for idx, i in enumerate(s):
            if d[i] == 1:
                return idx
        return -1
            