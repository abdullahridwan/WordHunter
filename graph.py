class Graph:
    def __init__(self):
        self.adj = {}
        self.visited = set()

    def addEdge(self, v, w):
      # check if v is in w first. if so, dont add end
      if w in self.adj and v in self.adj[w]:
        return
      if v in self.adj:
          self.adj[v].append(w)
      else:
          self.adj[v] = [w]
    def DFS(self, start, path, paths):
        path.append(start)
        paths.append(path.copy())
        if start in self.adj:
            for neighbor in self.adj[start]:
                if neighbor not in path:
                    self.DFS(neighbor, path, paths)
        path.pop()
