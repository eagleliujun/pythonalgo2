"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [ [1,2,3],
                [4,5,6],
                [7,8,9]], k = 1
Output:       [ [9,1,2],
                [3,4,5],
                [6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]


Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
"""
import math

class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        for i in range(k%(m*n)):
            self.shift_onestep_grid(grid, m)
        return grid

    def shift_onestep_grid(self, grid, m):

        for i in range(len(grid)-1):
            grid[i+1].insert(0, grid[i].pop())
        grid[0].insert(0, grid[m-1].pop())

    def shiftGrid2(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        step = k%(m*n)
        flat_list = self.flatten(grid)

        shifted_flat_list = flat_list[m*n-step:]
        shifted_flat_list.extend(flat_list[:m*n-step])
        grid = self.flat_array_to_grid(shifted_flat_list, m, n)

        return grid

    def flat_array_to_grid(self, arr, m, n):
        mat = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[i*n+j])
            mat.append(row)
        return mat


    def flatten(selfs, grid):
        a_list = []
        for arr in grid:
            for item in arr:
                a_list.append(item)
        return a_list


    def shiftGrid3(self, grid, k):
        m, n = len(grid), len(grid[0])
        k = k % (m * n)

        # res = [[None]*n for _ in range(m)]
        #
        # res = [[None] * n]*m
        res = [[None for _ in range(n)] for _ in range(m)]

        # print(res)
        for i in range(m):
            for j in range(n):
                y = (j + k) % n
                x = (i + (j + k) // n) % m
                res[x][y] = grid[i][j]

        # for arr in res:
        #     for item in arr:
        #         print(id(item))
        #
        return res


grid1 = [[1,2,3],[4,5,6],[7,8,9]]
#     = [[8,9,1],[2,3,4],[5,6,7]]
#
k1 = 2



# grid1 = [[1],[2],[3],[4],[7],[6],[5]]
# k1 = 23
#
# grid1 = [[1]]
# k1 = 100
mysolution = Solution()
print(mysolution.shiftGrid3(grid1, k1))



