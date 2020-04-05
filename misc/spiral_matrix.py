"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

class Solution:
    def spiral(self, m):
        if not m:
            return []
        row = len(m)
        col = len(m[0])
        seen = [[False] * col for _ in m]
        row_dir = [0, 1, 0, -1]
        col_dir = [1, 0, -1, 0]
        out = []
        r = c = dir_ind = 0
        for _ in range(row * col):
            out.append(m[r][c])
            seen[r][c] = True
            curr_row, curr_col = r + row_dir[dir_ind], c + col_dir[dir_ind]
            if 0 <= curr_row < row and 0 <= curr_col < col and not seen[curr_row][curr_col]:
                r, c = curr_row, curr_col
            else:
                dir_ind = (dir_ind + 1) % 4
                r,c = r + row_dir[dir_ind], c + col_dir[dir_ind]
        return out


def main():
    inp1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    inp2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    sol = Solution()
    assert sol.spiral(inp1) == [1,2,3,6,9,8,7,4,5]
    assert sol.spiral(inp2) == [1,2,3,4,8,12,11,10,9,5,6,7]


if __name__ == '__main__':
    main()