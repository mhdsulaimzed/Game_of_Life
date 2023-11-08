import time

ALIVE = " ■ " 
DEAD =  " ■ "


def get_grid(row, cols):
    return [[0 for _ in range(cols)] for _ in range(row)]


def get_alive_neighbor_count(grid, x, y):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
                if grid[x + i][y + j] == 1:
                    count += 1

    return count


def upgrade_grid(grid):
    updated_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbor_count = get_alive_neighbor_count(grid, x, y)

            if grid[x][y] == 1:
                # cell is currently alive
                if 2 == neighbor_count or neighbor_count == 3:
                    updated_grid[x][y] = 1  # cell remains alive
                else:
                    updated_grid[x][y] = 0  # cell dies
            else:
                # cell is currently dead
                if neighbor_count == 3:
                    updated_grid[x][y] = 1  # cell becomes alive
                else:
                    updated_grid[x][y] = 0  # cell remains dead
    return updated_grid


def display_grid(grid):
    display=""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                display += ALIVE + "\033[31m"
            else:
                display += DEAD + "\033[37m" 
        display += "\n"
    print(display)
        

def main():
    
    grid = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        

    for _ in range(50):
        print("\033c")   #for clearing terminal in each iteration
        display_grid(grid)
        time.sleep(0.7)
        grid = upgrade_grid(grid)


if __name__ == "__main__":
    main()
