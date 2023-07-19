# where x is either -1, 0, 1 and y is either -1, 0, 1
def checkAddEdge(grid, graph, x, y, i, j):
  if (x+i) < 0 or (y+j) < 0:
    return
  if (x+i) > 3 or (y+j) > 3:
    return
  node_start = grid[x][y]
  node_end = grid[x+i][y+j]
  graph.addEdge(node_start, node_end)

def addEdges(grid, graph, r: int, c: int):
  edge_costs = [-1, 0, 1]
  for i in edge_costs:
    for j in edge_costs:
      if i == 0 and j == 0:
        continue
      else:
        checkAddEdge(grid, graph, r, c, i, j)

