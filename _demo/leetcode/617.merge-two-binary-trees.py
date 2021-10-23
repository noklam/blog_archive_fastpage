#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        from collections import deque
        # Edge case where one tree is empty
        if not root1 and root2:
            return root1 or root2
            
        stack = deque()
        stack.append((root1, root2))

        while stack:
            nodes = stack.popleft()
            if nodes[0] is None or nodes[1] is None:
                continue

            nodes[0].val += nodes[1].val
            if nodes[0].left == None:
                nodes[0].left = nodes[1].left
            else:
                stack.append((nodes[0].left, nodes[1].left))

            if nodes[0].right == None:
                nodes[0].right = nodes[1].right
            else:
                stack.append((nodes[0].right, nodes[1].right))

        return root1  # @lc code=end
