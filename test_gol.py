from gol  import get_grid


def test_empty_grid():
  assert get_grid(3,3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
def test_one_cell_alive():
  
  grid=[[0, 0, 1], [0, 1, 0], [0, 0, 0]]
  x,y=1,1
  assert get_neighbour_count(grid,x,y) == 1