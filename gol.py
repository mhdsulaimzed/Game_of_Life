
def get_grid(row,cols):
   return [[0 for _ in range(cols)] for _ in range(row)]

def get_alive_neighbor_count(grid,x,y):
   count = 0
  
   for i in range(-1,2):
      for j in  range(-1,2):
            
            if i == 0 and j == 0:
               continue
            
            if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]):
                  if grid[x+i][y+j] ==  1:
                     count +=1

   return count

   
                
   

