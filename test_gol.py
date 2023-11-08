from gol  import get_grid,get_alive_neighbor_count,upgrade_grid


def test_empty_grid():
  assert get_grid(3,3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 

def test_one_cell_alive():
  rid=[[0, 0, 1], [0, 1, 0], [0, 0, 0]]
  x,y=1,1
  assert get_alive_neighbor_count(grid,x,y) == 1  


def test_multiple_alive_cell():
      grid=[[0, 0, 1 ], [1, 1, 0,], [1, 0, 0]]
      x,y = 1, 1
      assert get_alive_neighbor_count(grid,x,y) == 3


def test_rule_case1():
      grid=[[1, 1, 1 ], [1, 1, 0,], [0, 0, 0]]
      x, y = 1, 1
      assert upgrade_grid(grid) == [[1, 0, 1], [1, 0, 1], [0, 0, 0]]


def test_rule_case2():
    grid=[[1, 0, 1 ],[1, 0, 1],[0, 0, 0,]]
    assert upgrade_grid(grid) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 


def test_rule_case3():
    grid = [[1, 1, 0 ], [1, 0, 0,], [0, 0, 0]]
    assert upgrade_grid(grid) == [[1, 1, 0 ], [1, 1, 0,], [0, 0, 0]]




     



