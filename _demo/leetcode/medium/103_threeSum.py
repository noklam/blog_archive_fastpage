from typing import List
from collections import Counter, defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Complexity: O(N^2), iterate N twoSum problem.
        """
        if len(nums)<3:
            return []

        solution = []

        for i, v in enumerate(list(set(nums))):
            nums_subset = nums.copy()
            target = v
            nums_subset.remove(v)  # Can enhance with array, not important here
            tmp = self.twoSum(nums_subset, -target)
            solution = solution + tmp
        # print(solution)
        return list(set(solution))

    def twoSum(self, nums, target):
        """
        For two sum, the complexity is O(N), since we only scan the array once to match the hashmap
        n1 + n2  = target
        """
        solution = []
        hash_map = defaultdict(lambda: 0)
        for i, v in enumerate(nums):
            key = target - v
            hash_map[key] += 1

        for i, v in enumerate(nums):
            key = v
            if key in hash_map:
                if key ==target - v:
                    if hash_map[key] > 1:
                        solution.append(tuple(sorted([v, target - v, -target])))
                else:
                        solution.append(tuple(sorted([v, target - v, -target])))

        return solution



s = Solution()
inp = [-1, 0, 1, 2, -1, -4]
ans = s.twoSum(inp, 3)
ans = s.threeSum(inp)
print(ans)
