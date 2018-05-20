class Algorithm(object):
  
  HAS_CYCLE = False
  
  def calculateShortestPath(self, vertexList, edgeList, startVertex):
    
    startVertex.minDistance = 0
    
    for i in range(0,len(vertexList)-1):
      for edge in edgeList:
        
        u = edge.startVertex
        v = edge.targetVertex
        newDistance = u.minDistance + edge.weight
        
        if(minDistance < v.minDistance):
          v.minDistance = minDistance
          v.predecessor = u
          
    for edge in edgeList:
      if(self.hasCycle(edge)):
        print("Negative cycle detected...")
        self.HAS_CYCLE = True
        return
      
  def hasCycle(self, edge):
    if(edge.startVertex.minDistance + edge.weight) < (edge.targetVertex.minDistance):
      return True
    else:
      return False
      
  def getShortestPath(self, targetVertex):
    
    print("Shortes path to targetVertex: ", targetVertex.minDistance)
    
    node = targetVertex
    
    while(node):
      print("%s -> " % node.name)
      node = node.predecessor
