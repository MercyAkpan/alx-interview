#!/usr/bin/python3
""" THIS IS A ISLAND PERIMETER CALCULATION {M_I_N_E} """


def island_perimeter(grid):
    """This is the func. to find perimter of island"""

    perimeter = 0  # Initially make the perimeter = 0, then increase it on
    if len(grid) == 0:
        return perimeter
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4 - ((i > 0 and grid[i-1][j]) + (
                    i < len(grid)-1 and grid[i+1][j]) + (
                    j < len(grid[0])-1 and grid[i][j+1]) + (
                    j > 0 and grid[i][j-1]))
    return perimeter
# Example grid:
# grid = []
# grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# print(perimeter)
# NOTES: To be combined with 5-main.py,
#            say grids = [
#               [0, 1, 0, 0],
#               [1, 1, 1, 0],
#               [0, 1, 0, 0],
#               [1, 1, 0, 0]]
# Perimeter is +(4) when grids(i,j) is land[1] & -1 , when border is land.
# All surrounding border, is water[0], unless its land[1].
# e.g grids(0,1) is land[1] , so P = 4.
# Now only bottom of (0,1) is land[1], so P = 4-1 = 3
# For grids(1,1) is land[1], so P +=4 , P = 7
# Now every border around grids(1,1) is land [1], so P = 7-4 = 3
# For grids(2,2) is water[0], so Pis still = 3
