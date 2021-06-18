class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Right to Left addition, will reversed the list as solution at the end
        add_one = 1
        ans = []
        for i, d in enumerate(reversed(digits)):
            tmp = d + add_one
            add_one = tmp//10
            tmp = tmp % 10
            ans.append(tmp)
        
        if add_one:
            ans.append(1)
            
        return reversed(ans)
            
        
        