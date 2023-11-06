from gol  import get_grid


def test_empty_grid():
  assert get_grid(3,3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 