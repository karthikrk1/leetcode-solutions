"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


"""

class Solution:
    def rotate(self, m):
        for i in range((len(m) + 1) // 2):
            for j in range(len(m) // 2):
                temp = m[i][j]
                for _ in range(4):
                    j,i = len(m) - 1 - i, j
                    temp, m[i][j] = m[i][j], temp


def main():
    input_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    input_2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    output_1 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    output_2 = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]

    sol = Solution()
    sol.rotate(input_1)
    sol.rotate(input_2)
    assert input_1 == output_1
    assert input_2 == output_2


if __name__ == '__main__':
    main()
