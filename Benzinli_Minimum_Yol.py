

graph = {
  '1': {'3': 14, '2': 30},
  '2': {'1': 30, '5': 6, '6': 18},
  '3': {'1': 14, '4': 26, '7': 32},
  '4': {'3': 26, '5': 4, '6': 5},
  '5': {'4': 4, '2': 6, '7': 15},
  '6': {'2': 18, '4': 5, '7': 3},
  '7': {'6': 3, '5': 15, '3': 32}
  }

benzinlik={  '1': 0 ,  '2': 10,  '3': 0,  '4': 0,  '5': 0,  '6': 0,  '7': 0}

listex=[]

x=int(input("Baþlangýcta Depodaki benzin :"))

def find_all_paths(graph, start, end, path=[]): # tüm yollarý buluyoruz
        benzin=x
        cost=0
        path = path + [start]

        if start == end:
             #print(path)
             for i in range(0,len(path)-1):
                if i<len(path):
                    
                    
                    benzin=benzin-graph[path[i]][path[i+1]]  # olan benzinden gidilen yolun maliyetini çýkarýyoruz
                    cost=cost+graph[path[i]][path[i+1]]      # yol gidildikçe maliyeti güncelliyoruz
                    benzin=benzin+benzinlik[path[i]]         #eðer geçilen düðümde benzinlik var ise benzini o miktarda artýrýyoruz
            
             if benzin>0:                 # benzinin sýfýrdan büyük olduðu
                 k=(cost,benzin,path)
                 listex.append(k)
                 listex.sort()                       
        
        for node in graph[start]:
            if node not in path:
                find_all_paths(graph, node, end, path)
                

def yaz():
    print("Enkýsa Yol :",listex[0][2],"\t\tMaliyet :",listex[0][0],"\t\tKalan Benzin:",listex[0][1])

find_all_paths(graph, '1', '7')
yaz()








