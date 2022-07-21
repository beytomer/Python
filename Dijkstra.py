graph={
    'start': {'a': 4, 'b': 2}, 
    'a': {'start':4,'b': 3, 'c': 1, 'd': 7}, 
    'b': {'start':2,'a': 3, 'c': 5, 'd': 8}, 
    'c': {'a': 1, 'b': 5, 'd': 4, 'finish': 7}, 
    'd': {'a': 7, 'c': 4, 'b': 8, 'finish': 2}, 
    'finish': {'c':7,'d':2}
    }
def dijkstra(graph, bas, bit, visited=[], distances={}, predecessors={}):
  """ src içinde yönlendirilen en kýsa yol aðacýný hesaplar
  """

  if bas not in graph:
    raise TypeError('böyle bir il yok')
  if bit not in graph:
    raise TypeError('böyle bir il yok')

  if bas == bit:
    # En kýsa yolu oluþturur ve görüntüleriz
    path = []
    pred = bit
    while pred != None:
      path.append(pred)
      #print()
      #print("--------", pred, "-----------")
      #print()
      pred = predecessors.get(pred, None)  # ata dizisinde fýnýsh varmý varsa deðerini döndür yoksa none

    # yolu güzel bir þekilde görüntülemek için diziyi tersine çevirir.
    readable = path[0]
    for index in range(1, len(path)):  # tersten yazdýrarak sonucu elde ederiz
      readable = path[index] + '--->' + readable


    print("path: " + readable + ",   cost=" + str(distances[bit]))
  else:
    # ilk çalýþtýrma ise maliyeti baþlatýr.
    if not visited:  # sadece basta girer
      distances[bas] = 0

    # komsularý gez
    for neighbor in graph[bas]:
      if neighbor not in visited:
        new_distance = distances[bas] + graph[bas][neighbor]
        if new_distance < distances.get(neighbor, float('inf')):
          distances[neighbor] = new_distance

          predecessors[neighbor] = bas

    #print(distances, "             uzaklýk")
    #print(predecessors, "          atalarý")
    # ziyaret edildi olarak iþaretle
    visited.append(bas)  # visited uðranmamýþ komþulara uðruyor
    #print(visited, "               ziyaret edilen")

    # þimdi tüm komþular ziyaret edildi: tekrar
    # 'x' mesafeli en az ziyaret edilen düðümü seçin
    # Dijskstra'yý src = 'x' ile çalýþtýrýn
    unvisited = {}
    for k in graph:

      if k not in visited:
        #print(k)
        unvisited[k] = distances.get(k, float('inf'))
       # print(unvisited, "                 komþu olanlara deðerleri , olmayanlara sonsuz yazar")

    x = min(unvisited, key=unvisited.get)
    #print(x, "               min")
    #print()
    dijkstra(graph, x, bit, visited, distances, predecessors)



dijkstra(graph,'start', 'finish')
