

graph = {
    '1' : ['2','5'],
    '2' : ['3'],
    '3' : ['4'],
    '4' : ['1'],
    '5' : ['6'],
    '6' : ['7'],
    '7' : ['8'],
    '8' : ['5']

}

d=len(graph)

def rmvEdge(u, v):
    for i, k in enumerate(graph[u]):
        if k == v:
            graph[u].pop(i)


def printresult(u):
    for v in graph[u]:
        print(u,v)
        rmvEdge(u,v)
        printresult(v)

twin=False

node_path=[] # key'lerin çýkan ok sayýsý array5
path_to_the_node=[] # keylere gelen ok sayýsý
valuelist=[] # values kýsmýnýn listeye atýlmýþ hali

keylist=list(graph.keys()) 

for i in graph:
    valuelist.extend(graph[i])

for i in range(0,d):
    a=valuelist.count(keylist[i])
    path_to_the_node.append(a)

for i in graph:
    node_path.append(len(graph[i]))

for i in range(0,d):

    if node_path[i]==0 or path_to_the_node[i]==0:
        print("path not found !!")
        break

    elif node_path[i]-1 == path_to_the_node[i] :
        print(i+1,". starting node")
        printresult(keylist[i])
        break
    elif 1 :

        for j in range(0, d):
            if node_path[j]  == path_to_the_node[j] :
                twin=True

            else:

                twin=False

if twin==True:
    print("all double")
    printresult('1')
