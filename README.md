Sudoku Solver using Backtracking in python.

As a human being, we use the following steps to solve a sudoku.
Let us consider the number that we're checking for be the selected number "N" in this case.

The steps you would follow would be
- To check if N is in the column that you're in.
- To check if N is in the row that you're in.
- Finally, to check if N is in the 3x3 bordered box that you're in.

However, the approach to this problem is a little bit different in programming to reference, you can check demonstration.py.
The diagram below could help you understand this a little better.

![Screenshot 2024-03-08 at 10 57 49 PM](https://github.com/Shamitr-Mardikar/SudokuSolver/assets/73629015/3df7d457-6fe7-4faf-9698-9cc29dfb4268)


The approach we take in Python would be as follows :
- Firstly, we write a function that inputs the selected Number "N", it's X axis and it's Y axis. Next, it goes onto check if the current X axis paramater
  has N or not. It proceeds to do the same with the Y axis parameter as well. However one has to keep in mind that while checking the X-Axis, the Y axis isn't
  the same as the value you are iterating with and same goes for iterating through the Y axis. Because this would lead to an edge case where it would coincide
  with the N value itself and return False.
- Next, we have to write a function to check inside the 3x3 Box. Here, we take a very specific and cunning approach to the problem. We first take the 3x3 Box
  based off the current axes that N is in. Next, we do [(X-Axis or Y-Axis // 3) * 3]. The operation provides us the diagonal left top index from where we have to
  iterate inside the 3x3 box to check if any value has the same value as N.

Finally after finishing the approach, we write a display function to display the solved Sudoku.

The demonstration file however requires a nested list as the input Sudoku to work off. 
I'm currently working on a pyautogui program so that the code can also work on sudokus on the internet.
