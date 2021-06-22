    """
    https://leetcode.com/problems/number-of-matching-subsequences/
    #medium #array
    """


    class Solution:
    def numMatchingSubseq(self, full_str: str, words: List[str]) -> int:
        res = 0
        m = len(full_str)
        
        # A dict to cache result
        words_dict = Counter(words)
          
        for word, count in words_dict.items():
            n = len(word)
            # Skip if longer than the string to compare
            if n > m:
                continue
            else:
                idx = 0
                for c in full_str:
                    # Early breaking 
                    if idx == n:
                        res += count
                        break
                    # Increment if match
                    if c == word[idx]:
                        idx += 1
                else:                    
                    # Edge case in case it just match the char until the final char.
                    if idx == n:
                        res += count
                
        return res