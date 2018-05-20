from Dijkstra-Algorithm-in-Python import Vertex
from Dijkstra-Algorithm-in-Python import Edge
from Dijkstra-Algorithm-in-Python import Algorithm

node1 = Vertex("A")
node1 = Vertex("B")
node1 = Vertex("C")

edge1 = Edge(1,node1,node2)
edge2 = Edge(1,node2,node3)
edge3 = Edge(0.1,node1,node3)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)

vertexList = {node1,node2,node3}

algorithm = Algorithm()
algorithm.calculateShortestPath(vertexList, node1)
algorithm.getShortestPathTo(node3)

/*

And the output is

Shortest path to target is: 0.1
C ->
A ->

*/

/*

If we tried edge3 with 10 and the others remain the same,
the output is

Shortest path to target is: 2
C ->
B ->
A ->

*/
