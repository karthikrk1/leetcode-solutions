"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
from heapq import heapify, heappop, heappushpop, heappush

class Solution:
    def last_stone_weight(self, stones):
        if not stones:
            return 0
        heap = []
        heapify(heap)
        for i in stones:
            heappush(heap, ((-1) * i))

        while heap:
            # print(heap)
            max_1 = heappop(heap)
            try:
                max_2 = heappop(heap)
                diff = max_1 - max_2
                heappush(heap, diff)
            except:
                return -(max_1)
        return 0


def main():
    sol = Solution()
    inputs = [
        [2, 7, 4, 13, 8, 1],
        [1],
        [1, 3]
    ]
    out = []
    for input in inputs:
        out.append(sol.last_stone_weight(input))

    assert out == [1,1,2]


if __name__ == '__main__':
    main()
