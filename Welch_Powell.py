
graph={
    'A':{'B' ,'F' },
    'B':{'A' ,'C' ,'G'},
    'C':{'B' ,'D' },
    'D':{'C' ,'G' ,'E'},
    'E':{'D' ,'F' },
    'F':{'A' ,'E' ,'G'},
    'G':{'B' ,'D' ,'F'}
}
Colors=['Black','Blue','Brown','Green','Grey','Orange','Pink','Red','White','Yellow']

def Welch_Powell(graph):
     nodes = sorted(list(graph.keys()),key=lambda x:len(graph[x]), reverse=True)#Büyükten küçüðe doðru sýralý , en çok komþuluk olan dan en aza
     
     color_map = {}
     Paint={}
     available_colors = [True] * len(nodes)
     for node in nodes:#düðümleri gez
        for neighbor in graph[node]:#komsularýna bak
            if neighbor in color_map:#komþularý Color_map te var ise 
                color = color_map[neighbor]
                available_colors[color] = False
        for color, available in enumerate(available_colors):# color int sayi döndürür, available bool döndürür
            
            if available:
                color_map[node] = color
                Paint.setdefault(node,Colors[color])
                
                break
               
     print(color_map)
     print(Paint)


Welch_Powell(graph)