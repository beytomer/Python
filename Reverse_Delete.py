

graph1={
     '1' : {'3':14, '2':30},
     '2' : {'1':30, '5':6, '6':18},
     '3' : {'1':14, '4':26, '7':32},
     '4' : {'3':26, '5':4, '6':5},
     '5' : {'4':4, '2':6, '7':15},
     '6' : {'2':18, '4':5, '7':3},
     '7' : {'6':3, '5':15, '3':32} }

graph2={
    'A':{'B':5 ,'F':5,'S':3 },
    'B':{'A':5 ,'C':1 ,'G':2},
    'C':{'B':1 ,'D':3},
    'D':{'C':3 ,'G':3 ,'E':2},
    'E':{'D':2 ,'F':2},
    'F':{'A':5 ,'E':2 ,'G':3,'S':10},
    'G':{'B':2 ,'D':3 ,'F':3 },
    'S':{'A':3,'F':10 }}

graph3={     
    'A':{'B':5 ,'F':5 },
    'B':{'A':5 ,'C':1 ,'G':2},
    'C':{'B':1 ,'D':3},
    'D':{'C':3 ,'G':3 ,'E':2},
    'E':{'D':2 ,'F':2},
    'F':{'A':5 ,'E':2 ,'G':3,'S':10},
    'G':{'B':2 ,'D':3 ,'F':3 },
    'S':{'F':10 }}



graph4={
    's': {'a': 4, 'b': 2}, 
    'a': {'s':4,'b': 3, 'c': 1, 'd': 7}, 
    'b': {'s':2,'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'f': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'f': 2}, 
    'f': {'c':7,'d':2}
    }

graph5={
    'A':{'B':5 ,'F':5 },
    'B':{'A':5 ,'C':1 ,'G':2},
    'C':{'B':1 ,'D':3},
    'D':{'C':3 ,'G':3 ,'E':2},
    'E':{'D':2 ,'F':2},
    'F':{'A':5 ,'E':2 ,'G':3},
    'G':{'B':2 ,'D':3 ,'F':3 }
}

graph6 = {'s': {'a': 2, 'b': 1},
            'a': {'s': 2, 'b': 4, 'c':8},
            'b': {'s': 1, 'a': 4, 'd': 2},
            'c': {'a': 8, 'd': 7, 't': 4},
            'd': {'b': 2, 'c': 7, 't': 5},
            't': {'c': 4, 'd': 5}}


graph={
    'A':{'B':6 ,'G':3 },
    'B':{'A':6 ,'C':9 , 'D':7 , 'G':12},
    'C':{'B':9 ,'D':4},
    'D':{'B':7 ,'C':4  ,'E':11 ,'F':8 , 'G':18},
    'E':{'D':11 ,'F':13},
    'F':{'G':5 ,'D':8 ,'E':13},
    'G':{'A':3 , 'B':12,'D':18 ,'F':5 }
}

Keyler=list(graph.keys())
edges = []
s=[]
f=[]

kenarsay�lar� = []
silinecekler=[]
silinemezler=[]
parent = dict()
rank=dict()
komsular=dict()

print()

def komsuluklar�olustur(komsular):
    for i in graph.keys():

        komsular.setdefault(i,list(graph[i].keys()))
    #print("Komsular ",komsular)
    #print()

def parentiniolustur(parent,Keyler):
    for i in Keyler:
        parent.setdefault(i,i)
    #print(parent)
    #print()

def rank�n�olustur(rank,Keyler,kenarsay�lar�):
    j=0
    for i in Keyler:
        rank.setdefault(i,kenarsay�lar�[j])
        j+=1
    #print(rank)
    #print()

def rank�n�g�ncelle(parent,rank,n1,n2,komsular):
    rank[n1]=rank[n1]-1 # n1 = A : 2->1 ,       n1 = F : 2->1
    rank[n2]=rank[n2]-1 # n2 = F : 3->2 ,       n2 = G : 3->2
    komsular[n1].remove(n2) # A n�n komsular�ndan F yi sil , F n�n komsular�ndan G yi sil  ... 
    komsular[n2].remove(n1) # F nin komsular�ndan A y� sil , G nin komsular�ndan F yi sil  ...

    if rank[n1] <= 1 : 
        parent[n1]=komsular[n1][0] # A n�n yeni kom�usu komsuluk dizisinin ilk indisi yani B , F nin komsusu komsuluk dizisinin ilk indisi yani E
        N2=komsular[n1][0] # B yi al , F i�in E yi parent olarak ata
        rank[N2]=rank[N2]-1 # B nin rank�n� azalt , E yi azalt
        if rank[N2]<=1:  # B nin rank� 1 den k���kse , E nin rank� <=1 se
            komsular[N2].remove(n1)#E nin komsusunda F yi sil
            parent[N2]=komsular[N2][0] # E i�in di�er komsusu D yi Parent yap
            N1=komsular[N2][0] # D yi al 
            komsular[N1].remove(N2)
            rank[N1]=rank[N1]-1
       
    elif rank[n2] <= 1:
        parent[n2]=komsular[n2][0] 
        N1=komsular[n2][0]
        rank[N1]=rank[N1]-1
        if rank[N1]<=1:
            komsular[N1].remove(n2)
            parent[N1]=komsular[N1][0] # B yi di�er komsusunu Parent yap
            N2=komsular[N1][0]
            komsular[N2].remove(N1)
            rank[N2]=rank[N2]-1




def reverse(graph):
    for i in graph:
        j=0
        while j < len(graph[i].values()):#graph[i] nin degerlerinin say�s�
            s=list(graph[i].values())    #graph[i] nin komsular�n�n say� degerleri
            f=list(graph[i].keys())      #graph[i] nin komsular� yani value harfleri
            k = (s[j],i,f[j])            #k burada bir tuple 
            j=j+1
            edges.append(k)                # herseferinde olu�turdu�umuz tuple '� edges listemize ekledik
    edges.sort()                       # edges listemizi s�ralad�k k���kten b�y��e do�ru    
    EdgeControl(edges)
    
    for i in Keyler:
        kenarsay�lar�.append(len(graph[i]))       #her d���m�n ka� kenar say�s� var
    #print(kenarsay�lar�)    
    #print()
    komsuluklar�olustur(komsular)
    #print(komsular)
    parentiniolustur(parent,Keyler)
    rank�n�olustur(rank,Keyler,kenarsay�lar�)
    #print()
    edges.reverse()#k���kten b�y��e olan s�ralmay� ters cevirdim suan dizi buyukten kucuge do�ru s�ral�
    print("BASLANGIC",edges)
    #print()
    for edge in edges:   # burda ba�lang�cta tek kenara sahip olan d���m� tesbit edip listeden c�karaca��z
        w1,n1,n2=edge
        if rank[n1]==1 or rank[n2] == 1:
            edges.remove(edge)
            silinemezler.append(edge)
            rank[n1]=rank[n1]-1
            rank[n2]=rank[n2]-1
    #print("TEK d���ml�  olan silinince",edges)
    
    kenarc�kar(edges,rank,parent,komsular,silinecekler,silinemezler)
  

   
    
def EdgeControl(edges):
    for edge in edges:
            w1,n1,n2=edge
            Z=(w1,n2,n1)
            if Z in edges:#tersi varsa tersini ��kar
                edges.remove(Z)
            else:
                None



def kenarc�kar(edges,rank,parent,komsular,silinecekler,silinemezler):#{'A': 2, 'B': 3, 'C': 2, 'D': 3, 'E': 2, 'F': 3, 'G': 3}
    print()#[(5, 'A', 'F'), (5, 'A', 'B'), (3, 'F', 'G'), (3, 'D', 'G'), (3, 'C', 'D'), (2, 'E', 'F'), (2, 'D', 'E'), (2, 'B', 'G'), (1, 'B', 'C')]
    for edge in edges:#
        w1,n1,n2=edge
        #print()
        if rank[n1] > 1 and rank[n2] > 1:
            #print(edge,"a l � n d �")
            silinecekler.append(edge)
            #print(edge,"        s i l i n d i")  
            rank�n�g�ncelle(parent,rank,n1,n2,komsular)
        
        elif  rank[n1] <= 1 and rank[n2] > 1  :
            #print(edge,"a l � n d �")
            silinemezler.append(edge)
            #print(n1,n2,"   bu kenar silinemez")
            

        elif  rank[n1] > 1 and rank[n2] <= 1:
            #print(edge,"a l � n d �")
            silinemezler.append(edge)
            #print(n1,n2,"   bu kenar silinemez")
        else:
            #print(edge,"a l � n d �")
            silinemezler.append(edge)
           # print(n1,n2,"   bu kenar silinemez")
    
    print(silinecekler,"S�L�NECEK KENARLAR","\n\n",silinemezler,"S�L�NEMEYECEK KENARLAR")
    
    


print()
reverse(graph)

