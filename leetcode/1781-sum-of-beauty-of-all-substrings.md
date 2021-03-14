# 1781. Sum of Beauty of All Substrings

[https://leetcode.com/problems/sum-of-beauty-of-all-substrings/discuss/1096457/python-on2-with-counter](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/discuss/1096457/python-on2-with-counter)



Complexity: O\(N^2 \* 26\)

  
Two Loop + maximum 26 key\(lower case dictionary\) to find Min/Max.

Since This question has a constrain with length &lt;=500, so this answer is reasonable. We can eliminate the use of dict to find Max/Min if needed.  


```python
from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0

        for i in range(len(s)):
            sub_str = s[i:]
            c = Counter(sub_str)
			
            for j in range(len(sub_str) - 1, 0, -1):
                # Start from longer string, slight performance gain for long repeating string
                if len(c.keys()) <=1 : break
                beauty = c.most_common()[0][1] - c.most_common()[-1][1]
                c[sub_str[j]] -= 1
                if c[sub_str[j]] == 0:
                    del c[sub_str[j]]  # Avoid counting 0, delete the key
                total_beauty = beauty + total_beauty

        return total_beauty
```

