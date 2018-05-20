import heapq

def calculateShortestPath(self, vertexList, startVertex):
  
  queue = []
  startVertex.minDistance = 0
  heapq.heappush(queue, startVertex)
  
  while(len(queue) > 0):
    actualVertex = heapq.heappop(queue)
    
    for edge in actualVertex.adjacenciesList:
      u = edge.startVertex
      v = edge.targetVertex
      minDistance = u.minDistance + edge.weight
      
      if(minDistance < v.minDistance):
        v.predecessor = u
        v.minDistance = newDistance
        heapq.heappush(queue, v)
        
def getShortestPathTo(self, targetVertex):
  
  print("Shortes path to target is: ", targetVertex.minDistance)
  
  node = targetVertex
  
  while(node):
    print("%s -> " % node.name)
    node = node.predecessor
