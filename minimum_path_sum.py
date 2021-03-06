"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which 
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any 
point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes 
the sum.
"""
#dynamic programming

def min_path_sum(grid):
    if not grid:
          return 0

    rows = len(grid)
    cols = len(grid[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = grid[0][0] #top left

    for i in range(1,cols): #first row
      dp[0][i] = dp[0][i-1] + grid[0][i] 

    for i in range(1, rows): #first column
      dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, rows):
      for j in range(1, cols):
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[rows-1][cols-1]