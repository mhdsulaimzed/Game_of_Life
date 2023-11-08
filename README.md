
# Conway's Game of Life 
This Python program For Conway's Game of Life, a cellular automaion that evolves over time according to a set of rules. and was developed using Test-Driven Development (TDD)

## Requirements
- Python 3

## Usage
Run the `main()` function to start the simulation. The simulation will run for 50 iterations and display the grid state after each iteration.

## Understanding the Code
The code consists of four main functions:

- `get_grid(row, cols)`: Initializes a grid of the specified dimensions with all cells dead (0).
- `get_alive_neighbor_count(grid, x, y)`: Counts the number of alive neighbors of a given cell (x, y) in the grid.
- `upgrade_grid(grid)`: Applies the rules of Conway's Game of Life to update each cell in the grid based on its current state and the number of alive neighbors.
- `display_grid(grid)`: Prints the current state of the grid to the console using escape sequences for giving them a colour.

## Rules of Conway's Game of Life
- Any alive cell with fewer than two alive neighbors dies, as if caused by underpopulation
- Any alive cell with two or three alive neighbors lives on to the next generattion
- Any alive cell with more than three alive neighbors dies by overpopulation
- Any dead cell with exactly three alive neighbors becomes a alive cell

## Initial Grid Pattern
The simulation starts with a specific initial grid pattern This pattern will evolve into a interesting pattern over time.

## Visualization
The simulation displays the grid state after each iteration using color-coded blocks:
- `■`: Alive cell
- `■`: Dead cell
both have different color while printing, Dead cells are printed in White and the alive once in Red 

## Experimentation
You can experiment with different initial grid patterns to observe the resulting patterns and behaviors of the simulation.
