# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# 1786. Number of Restricted Paths From First to Last Node

# Notes for myself:
# I correctly use BFS and distanceToLastNode for the main logic to solve this question.
# However, I don't know about Dijikstra, so I cannot come up with an implemntation of the
# distancetoLastNode function. This is a good example to get me started to learn more about
# Graph Algorithm.

# This is a good introduction for Dijikstra
# https://www.youtube.com/watch?v=pVfj6mxhdMw

# Generic Dijkstra

import math
from heapq import heappush, heappop
from functools import lru_cache

class GG:
    def dijkstra(self, graph, source):
        n = len(graph)
        vis = [False] * n
        weig = [math.inf] * n
        weig[source] = 0
        pq = []
        heappush(pq, (0, source))
        while pq:
            d, u = heappop(pq)
            vis[u] = True
            for v, w in graph[u]:
                if not vis[v]:
                    nd = d + w
                    if nd < weig[v]:
                        weig[v] = nd
                        heappush(pq, (nd, v))
        return weig


class Solution:
    def countRestrictedPaths(self, n, edges):
        # build graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))

        # get the shortest distance from all sources to target
        # this uses Dijkstra
        gg = GG()
        path_sums = gg.dijkstra(graph, n - 1)

        # dp(u) is all restricted paths from vertex-u to target
        @lru_cache(None)
        def dp(u):
            if u == n - 1:
                return 1
            ans = 0
            for v, _ in graph[u]:
                if path_sums[v] < path_sums[u]:
                    ans = ans + dp(v)
                    ans = ans % (10 ** 9 + 7)
            return ans

        return dp(0)


if __name__ == "__main__":
    test_cases = [
        (
            5,
            [
                [1, 2, 3],
                [1, 3, 3],
                [2, 3, 1],
                [1, 4, 2],
                [5, 2, 2],
                [3, 5, 1],
                [5, 4, 10],
            ],
        )
    ]

    for test_case in test_cases:
        print(test_case, "\nanswer: ", Solution().countRestrictedPaths(*test_case))
        print("=================================")

