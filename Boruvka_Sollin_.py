
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

for i in range(0,len(graph3.keys())):   #setgraph adüğümleri atıyoruz
	setgraph.append([i])                #sonrada içinde dolaşabilmek için dizi olarak ekledik
def birlestir(e):                       # alınan düğümleri setgraph dan sileriz	                                    
                                      # ve graphda gidilen düğümleri de görmemizi sağlar
	e0 = -1
	e1 = -1
	for i in range(0,len(setgraph)):
		if e[0] in setgraph[i]:
			e0 = i
		if e[1] in setgraph[i]:
			e1 = i
	setgraph[e0] =setgraph[e0]+ setgraph[e1]
	del setgraph[e1]
print("Düğümler : " , setgraph)
while (len(setgraph) > 1):
	edges = []
	for j in setgraph:       # burada j [1] şeklide dizilerdir
		m = [999,[0,0]]      #[iki düğüm arası maliyet,[1.düğüm,2.düğüm]]
		for vertex in j:     # vertex düğümlere bakar j nin içinde olana

			a=list(graph3[vertex])      # düğümlerimizin komşuları a'ya eşittir

			for i in a:
				if i not in j and graph3[vertex][i] != 0:
					if (m[0] > graph3[vertex][i]):
						m[0] = graph3[vertex][i]
						m[1] = [vertex,i]
		if (m[1][0] > m[1][1]):
			m[1][0], m[1][1] =  m[1][1],m[1][0]
		if (m[1] not in edges):
			edges.append(m[1])
	for e in edges:                 # her seferinde yukarıda oluşturduğumuz edges
		                            # dizindeki kenarları birleştir fonksiyonuna yollarız

		birlestir(e)


	print("Seçilen Kenarlar: " ,edges)

	
