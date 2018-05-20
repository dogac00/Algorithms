from Bellman-Ford-Algorithm-in-Python import Algorithm
from Bellman-Ford-Algorithm-in-Python import Node
from Bellman-Ford-Algorithm-in-Python import Edge

node1 = Node("A")
node1 = Node("B")
node1 = Node("C")
node1 = Node("D")

edge1 = Edge(1,node1,node2)
edge2 = Edge(1,node2,node3)
edge3 = Edge(1,node3,node4)
edge4 = Edge(4,node3,node2)
edge5 = Edge(300,node1,node4)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node2.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge4)
node3.adjacenciesList.append(edge5)

vertexList = [node1,node2,node3,node4]
edgeList = [edge1,edge2,edge3,edge4,edge5]

algorithm = Algorithm()
algorithm.calculateShortestPath(vertexList, edgeList, node1)
algorithm.getShortestPath(node4)

"""

The output is:

Shortest path to targetVertex: 3
D ->
C ->
B ->
A ->

"""

# With edge5 is 0.001

"""

The output is:

Shortest path to targetVertex: 0.001
D ->
A ->

"""
