"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    def setZeroes(self, matrix):
        """Modify inplace"""
        is_col = False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, col):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if not matrix[0][0]:
            for j in range(col):
                matrix[0][j] = 0

        if is_col:
            for i in range(row):
                matrix[i][0] = 0


def main():
    mat1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    mat2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    sol = Solution()
    sol.setZeroes(mat1)
    sol.setZeroes(mat2)

    out1 = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]

    out2 = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]

    assert mat1 == out1
    assert mat2 == out2


if __name__ == '__main__':
    main()