"""
Complexity  O(N * LogN) + O(K * LogN)
1. We need to sorted the list once
2. Then for each update, we need to insert the tuple in an ordered list (Log N) * k

# Learning point
* A heap would simplify the implementation a lot, as I am basically implementing heap here.
* list.pop(0) is O(n) while deque.popleft() is O(1)
"""
from typing import List
from bisect import insort


def average(classes):
    ratios = []
    for i in classes:
        ratios.append(i[0] / i[1])
    return sum(ratios) / len(ratios)


def delta(x, y):
    return -(y - x) / (y ** 2 + y)


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        order = []
        for x in classes:
            order.append(delta(x[0], x[1]))
        d = []
        for i, v in enumerate(order):
            t = tuple([v,i])
            d.append(t)
        order = sorted(d)
        while extraStudents > 0 and order:
            selected_tuple = order.pop(0)
            value,index  = selected_tuple

            c = classes[index]
            pass_, total_ = c
            if pass_ == total_:
                continue
                
            c[0] = pass_ + 1
            c[1] = total_ + 1
            extraStudents = extraStudents - 1
            
            new_value = delta(c[0], c[1])
            new_tuple = (new_value, index, )
            insort(order, new_tuple)
            if extraStudents <= 0:
                break
        return average(classes)
"""python
A better solution from discuss
```python
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b

        maxHeap = []
        for a, b in classes:
            a, b = a * 1.0, b * 1.0  # Convert int to double
            maxHeap.append((-profit(a, b), a, b))
        heapq.heapify(maxHeap)  # Heapify maxHeap cost O(N)

        for _ in range(extraStudents):
            d, a, b = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-profit(a + 1, b + 1), a + 1, b + 1))

        return sum(a / b for d, a, b in maxHeap) / len(classes)
```

if __name__ == "__main__":
    test_case = []

    for test_case in test_cases:
        print(test_case, Solution().maxAverageRatio(test_case, 4))
        print("=================================")

