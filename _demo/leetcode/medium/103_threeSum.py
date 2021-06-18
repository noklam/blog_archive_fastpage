from typing import List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Complexity: O(N^2), iterate N twoSum problem.
        """
        if not nums:
            return []

        hash_map = {}
        solution = []

        for i, v in enumerate(nums):
            if hash_map.get(v):
                hash_map[v] += 1
            else:
                hash_map[v] = 1

        for i, v in enumerate(nums):
            nums_subset = nums.copy()
            hash_map_subset = hash_map.copy()
            hash_map_subset[v] -= 1
            target = nums_subset.pop(i)  # Can enhance with array, not important here
            tmp = self.twoSum(nums, target)
            solution = solution + tmp
        # print(solution)
        return list(set(solution))

    def twoSum(self, nums, target):
        """
        For two sum, the complexity is O(N), since we only scan the array once to match the hashmap
        n1 + n2 + target = 0
        n1 + n2 = -target
        """
        solution = []
        hash_map = {}
        for i, v in enumerate(nums):
            key = -target - v
            print("key", target, key, v, "***", key + target + v)
            if hash_map.get(key):
                hash_map[key] += 1
            else:
                hash_map[key] = 1

        for i, v in enumerate(nums):
            if v in hash_map:
                if -target - v  == v:
                    if hash_map[v] > 1:
                        print("a", target, v, hash_map[v])
                        solution.append(tuple(sorted([v, hash_map[v], target])))
                    else:
                        print("s", target, v, hash_map[v])
                        solution.append(tuple(sorted([v, hash_map[v], target])))

        return solution


s = Solution()
inp = [-1, 0, 1, 2, -1, -4]
ans = s.twoSum(inp, -10)
print(ans)
