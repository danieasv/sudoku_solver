import numpy as np
import time

class Sudoku_solver:
    def __init__(self, grid):
        self.grid=np.array(grid)


    def solve(self, grid, y, x):

        x_new = x
        y_new = y
        #print("x:{}, y:{}".format(x,y))
        while self.grid[y_new, x_new] != 0 or (x_new == x and y_new == y):

            # Search for next zero coordinate
            if x_new < 8:
                x_new += 1
            elif y_new < 8:
                x_new = 0
                y_new += 1


            else:
                for num in range(1, 10):
                    new_grid = np.copy(grid)
                    new_grid[y, x] = num
                    #print(new_grid)
                    if self.verify(new_grid):
                        self.grid=new_grid
                        return True
                return False

        if x_new < 8:
            for num in range(1, 10):
                new_grid = np.copy(grid)
                new_grid[y_new, x_new] = num
                if self.solve(new_grid, y_new, x_new):
                     return True

        elif y_new < 8:
            for num in range(1, 10):
                new_grid = np.copy(grid)
                new_grid[y_new, x_new] = num
                if self.solve(new_grid, y_new, x_new):
                    return True



    def verify(self,grid,y,x):
        is_solution = True

        # verify row
        for row in grid[:y,:]:
            print(row)
            for num in range(1,10):
                if not num in row:
                    is_solution = False

        # verify column
        for col in grid.T:
            for num in range(1,10):
                if not num in col:
                    is_solution = False

        #verify boxes
        for rowsnum in range(0,3):
            rows = np.arange(3*rowsnum, 3*rowsnum + 3)
            for colsnum in range(0,3):
                cols = np.arange(3 * colsnum,3 * colsnum + 3)
                for num in range(1,10):
                    if not num in grid[3*rowsnum: 3*rowsnum + 3, 3*colsnum: 3*colsnum + 3]:
                        is_solution = False

        return is_solution

grid = [[9,5,6,7,4,3,1,8,0],
        [3,8,7,1,5,0,6,9,4],
        [4,1,0,9,8,6,7,5,3],
        [1,7,4,5,0,9,8,3,6],
        [0,3,5,8,6,4,9,1,7],
        [6,9,8,3,7,1,0,4,5],
        [7,4,9,2,3,8,5,6,1],
        [5,6,1,4,9,7,3,2,8],
        [8,2,3,6,1,5,4,7,9]]
grid = np.array(grid)
counter = np.count_nonzero(grid==0)
start = time.time()

grid =np.array( [[1,2,3],[4,5,6], [7,8,9] ])
sod = Sudoku_solver(grid)
sod.verify(grid,1,1)
#sod.solve(grid,-1,-1)
end = time.time()

print("Runtime with {} unknown: {}".format(counter,end - start))
