graph={
    'start': {'a': 4, 'b': 2}, 
    'a': {'start':4,'b': 3, 'c': 1, 'd': 7}, 
    'b': {'start':2,'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'finish': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'finish': 2}, 
    'finish': {'c':7,'d':2}
    }
def dijkstra(graph, bas, bit, visited=[], distances={}, predecessors={}):
  """ src i�inde y�nlendirilen en k�sa yol a�ac�n� hesaplar
  """

  if bas not in graph:
    raise TypeError('b�yle bir il yok')
  if bit not in graph:
    raise TypeError('b�yle bir il yok')

  if bas == bit:
    # En k�sa yolu olu�turur ve g�r�nt�leriz
    path = []
    pred = bit
    while pred != None:
      path.append(pred)
      #print()
      #print("--------", pred, "-----------")
      #print()
      pred = predecessors.get(pred, None)  # ata dizisinde f�n�sh varm� varsa de�erini d�nd�r yoksa none

    # yolu g�zel bir �ekilde g�r�nt�lemek i�in diziyi tersine �evirir.
    readable = path[0]
    for index in range(1, len(path)):  # tersten yazd�rarak sonucu elde ederiz
      readable = path[index] + '--->' + readable


    print("path: " + readable + ",   cost=" + str(distances[bit]))
  else:
    # ilk �al��t�rma ise maliyeti ba�lat�r.
    if not visited:  # sadece basta girer
      distances[bas] = 0

    # komsular� gez
    for neighbor in graph[bas]:
      if neighbor not in visited:
        new_distance = distances[bas] + graph[bas][neighbor]
        if new_distance < distances.get(neighbor, float('inf')):
          distances[neighbor] = new_distance

          predecessors[neighbor] = bas

    #print(distances, "             uzakl�k")
    #print(predecessors, "          atalar�")
    # ziyaret edildi olarak i�aretle
    visited.append(bas)  # visited u�ranmam�� kom�ulara u�ruyor
    #print(visited, "               ziyaret edilen")

    # �imdi t�m kom�ular ziyaret edildi: tekrar
    # 'x' mesafeli en az ziyaret edilen d���m� se�in
    # Dijskstra'y� src = 'x' ile �al��t�r�n
    unvisited = {}
    for k in graph:

      if k not in visited:
        #print(k)
        unvisited[k] = distances.get(k, float('inf'))
       # print(unvisited, "                 kom�u olanlara de�erleri , olmayanlara sonsuz yazar")

    x = min(unvisited, key=unvisited.get)
    #print(x, "               min")
    #print()
    dijkstra(graph, x, bit, visited, distances, predecessors)



dijkstra(graph,'start', 'finish')
