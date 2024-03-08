grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def check(x_axis, y_axis, n):
        for i in range(0,9):
            if grid[i][x_axis] == n and i!=y_axis: #Checks to see if the number exists in any X Axis
                  return False
            
        for i in range(0,9):
              if grid[y_axis][i] == n and i!=x_axis: #Checks to see if the number exists in any Y Axis
                  return False
              
        x0 = (x_axis//3) * 3  
        y0 = (y_axis//3) * 3

        for x_axis in range(x0, x0+3):
            for y_axis in range(y0, y0+3):
                if grid[y_axis][x_axis] == n:
                    return False
        
        return True

def display(matrix):
     for i in range(9):
          print(matrix[i])

def solution_backtrack():
    global grid
    for y in range(9):
          for x in range(9):
               if grid[y][x] == 0:
                    for n in range(1,10):
                         if check(x, y, n):
                              grid[y][x] = n
                              solution_backtrack() #Moves onto the next index and keeps indexing through Sudoku
                              grid[y][x] = 0 # BACKTRACKING #If solution keeps returning false, you come back and revert to inital value to go through again
                    return
    print(grid)
    input('More?')

solution_backtrack()
display(grid)

               