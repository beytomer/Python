
graph = {
	0:{1:9, 2:75, },
	1:{0:9, 2:95, 3:19,4:42},
	2:{0:75,1:95,3:51},
	3:{1:19,2:51,4:31},
	4:{1:42,3:31}
}

graph2 = {

	0:{1:2,5:1},
	1:{0:2,2:4,6:3},
	2:{1:4,3:6},
	3:{2:6,4:1,6:1},
	4:{3:1,5:7},
	5:{0:1,4:7,6:4},
	6:{1:3,3:1,5:4}


}

graph3 = {
    
    0:{1:7,5:5},
    1:{0:7,2:1,6:2},
    2:{1:1,3:8,},
    3:{2:8,4:2,6:5},
    4:{3:2,5:3,},
    5:{4:3,6:4,0:5},
    6:{5:4,3:5,1:2}   
}
setgraph = []

for i in range(0,len(graph3.keys())):   #setgraph ad���mleri at�yoruz
	setgraph.append([i])                #sonrada i�inde dola�abilmek i�in dizi olarak ekledik
def birlestir(e):                       # al�nan d���mleri setgraph dan sileriz	                                    
                                      # ve graphda gidilen d���mleri de g�rmemizi sa�lar
	e0 = -1
	e1 = -1
	for i in range(0,len(setgraph)):
		if e[0] in setgraph[i]:
			e0 = i
		if e[1] in setgraph[i]:
			e1 = i
	setgraph[e0] =setgraph[e0]+ setgraph[e1]
	del setgraph[e1]
print("D���mler : " , setgraph)
while (len(setgraph) > 1):
	edges = []
	for j in setgraph:       # burada j [1] �eklide dizilerdir
		m = [999,[0,0]]      #[iki d���m aras� maliyet,[1.d���m,2.d���m]]
		for vertex in j:     # vertex d���mlere bakar j nin i�inde olana

			a=list(graph3[vertex])      # d���mlerimizin kom�ular� a'ya e�ittir

			for i in a:
				if i not in j and graph3[vertex][i] != 0:
					if (m[0] > graph3[vertex][i]):
						m[0] = graph3[vertex][i]
						m[1] = [vertex,i]
		if (m[1][0] > m[1][1]):
			m[1][0], m[1][1] =  m[1][1],m[1][0]
		if (m[1] not in edges):
			edges.append(m[1])
	for e in edges:                 # her seferinde yukar�da olu�turdu�umuz edges
		                            # dizindeki kenarlar� birle�tir fonksiyonuna yollar�z

		birlestir(e)


	print("Se�ilen Kenarlar: " ,edges)

	
