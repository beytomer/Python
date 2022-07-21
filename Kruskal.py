
graph={
    'A':{'B':5 ,'F':5 },
    'B':{'A':5 ,'C':1 ,'G':2},
    'C':{'B':1 ,'D':3},
    'D':{'C':3 ,'G':3 ,'E':2},
    'E':{'D':2 ,'F':2},
    'F':{'A':5 ,'E':2 ,'G':3},
    'G':{'B':2 ,'D':3 ,'F':3 }
}

graph2={
    'A':{'B':7 ,'D':5 },
    'B':{'A':7 ,'C':8 ,'D':9,'E':7},
    'C':{'B':8 ,'E':5},
    'D':{'A':5 ,'B':9 ,'E':7,'F':6},
    'E':{'B':7,'C':5,'D':7 ,'F':8,'G':9},
    'F':{'D':6 ,'E':8 ,'G':11},
    'G':{'E':9 ,'F':11 }
}


graph7={
    's': {'a': 4, 'b': 2}, 
    'a': {'s':4,'b': 3, 'c': 1, 'd': 7}, 
    'b': {'s':2,'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'f': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'f': 2}, 
    'f': {'c':7,'d':2}
    }


graph8 = {'s': {'a': 2, 'b': 1},
            'a': {'s': 2, 'b': 4, 'c':8},
            'b': {'s': 1, 'a': 4, 'd': 2},
            'c': {'a': 8, 'd': 7, 't': 4},
            'd': {'b': 2, 'c': 7, 't': 5},
            't': {'c': 4, 'd': 5}}


Vertices=list(graph.keys())
edges = []
s=[]
f=[]
minimum_spanning_tree = []
parent = dict()
rank = dict()

def make_set(node):
    parent[node] = node #Burada her d���me kendisini parent diye atad� PARENT = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G'}
    rank[node] = 0  # HEr d���m�n de�erini baslarken 0 olarak atad� RANK = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
    #print(parent)
    #print(rank)


def find(node): # atas� olmayanlara kendisini ata olarak d�d�r�r
    if parent[ node] != node:  # yani d���m�n atas� kendisi de�ilse 
        parent[node] = find(parent[node])
    return parent[node] # o d���m�n in PARENT ini d�nd�r�r


def union(node1, node2):
    root1 = find(node1)  #burda bir daha kontrol edilmesinin nedeni parazit d�ng� olu�turmamak
    root2 = find(node2)

    #print(root1,root2) # A D , C E , D F , D B , D E , E G
    if root1 != root2:
        if rank[root1] > rank[root2]:  # root1 in degeri root2 den B�Y�K OLMADIGI S�RECE root2 nin parentine root1 ata
            parent[root2] = root1
        else:
            parent[root1] = root2       # di�er durumlarda root1 in parenti her zaman root2
            #print(parent)               # {'A': 'D', 'B': 'D', 'C': 'E', 'D': 'E', 'E': 'E', 'F': 'D', 'G': 'G'}
        if rank[root1] == rank[root2]:
            rank[root2] += 1
            #print(rank)


def kruskal(graph):
    for i in graph:
        j=0
        while j < len(graph[i].values()):#graph[i] nin degerlerinin say�s�
            s=list(graph[i].values())    #graph[i] nin komsular�n�n say� degerleri
            f=list(graph[i].keys())      #graph[i] nin komsular� yani value harfleri
            k = (s[j],i,f[j])            #k burada bir tuple 
            j=j+1
            edges.append(k)                # herseferinde olu�turdu�umuz tuple '� edges listemize ekledik
    edges.sort()                       # edges listemizi s�ralad�k k���kten b�y��e do�ru
    

    for node in Vertices:
        make_set(node)          # bu fonksiyon cagr�larak b�t�n d���mler ba�lang��ta rank� = 0 de�erine atan�r ve Parentleri de kendileri olarak atanm�� olur 
        
  

    
    for edge in edges: # Edges listesi i�inde dolan
        weight, node1, node2 = edge #  ve edge in  her bir eleman�n� ( weight , vertice1 , vertice2 ) �eklinde ata
        if find(node1) != find(node2):  # find fonksiyonu edges listesindeki ikili durumlardan birtanesini parent kontrolu yaparak elenmesini sa�lar yani atas� ayn� olanlar� alm�yor  �rn: (1,s,b) , (1,2,s) ... 
            union(node1, node2)
            #print(union(node1,node2))
            minimum_spanning_tree.append(edge)

    return sorted(minimum_spanning_tree)



print (kruskal(graph))