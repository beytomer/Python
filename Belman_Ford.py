
graph2 = {

	0:{1:-1,2:4},
	1:{2:3,3:2,4:2},
	3:{2:5,1:2},
	4:{3:-3}
}
V=5
graph = []
for i in graph2.keys():  #graph dizisine [1.node,2.node,aralar�ndaki de�er ]�eklinde dizi ekliyoruz
    for j in graph2[i]:
        graph.append([i, j, graph2[i][j]])

def printArr( dist):
    print("dugumlerin degeri")
    for i in range(V):
        print("% d \t\t % d" % (i, dist[i]))

def BellmanFord( src):

    dist = [float("Inf")] * V # her eleman�n de�eri sonsuz
    dist[src] = 0

    for i in range(V - 1):  #uzakl�klar� g�ncelle

        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                dist[v] = dist[u] + w

    for u, v, w in graph:
         if dist[u] != float("Inf") and dist[u] + w < dist[v]:
             print("Graph contains negative weight cycle")

             return

    printArr(dist)

BellmanFord(0)

