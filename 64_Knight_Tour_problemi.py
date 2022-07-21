
n = 8
def isSafe(x, y, board):
    '''
        �, j'nin ge�erli dizinler olup olmad���n� kontrol etmek i�in bir yard�mc� i�lev
�������� N * N satran� tahtas� i�in
    '''
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False


def printSolution(board):
    '''
       Satran� tahtas� matrisini basmak i�in bir yard�mc� i�lev
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT():
    

    
    board = [[-1 for i in range(n)] for i in range(n)]# sekize sekizlik bir matris olu�turarak i�ine -1 yerle�tirir hepsinin

    #move_x ve move_y, Knight'�n bir sonraki hamlesini tan�mlar.
    # move_x, bir sonraki x koordinat� de�eri i�indir
    # move_y, y koordinat�n�n sonraki de�eri i�indir
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # at ba�lang��ta ilk blokta oldu�undan
    board[0][0] = 0

    # at�n konumu i�in ad�m sayac�
    pos = 1

   
    if (not solveKTUtil(board, 0, 0, move_x, move_y, pos)):# E�er solveKTUtil den d�nen de�er TRUE ( TRUE olmas� demek pos == n ** 2 yani i�lemler sonland� t�m board gezildi ) ise if ( not TRUE) ise else i yazd�r�r yani tahtan�n son halini basar  
        print("Solution does not exist") # E�er solveKTUtil den d�nen deger FALSe ise ( ancak i�lemler bitmeden �nce c�k�lmas� durumu yani return FALSE degeri d�n�nce)     if ( not FALSE ) ise if i�erisini yazd�racak
    else:
        printSolution(board)


def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos):
    '''
        Knight Tour'u ��zmek i�in tekrarlayan bir yard�mc� fonksiyon
�������� 
    '''

    if (pos == n ** 2):# e�er t�m kareler dola��ld�ysa yani board tamamen gezildiyse true d�nd�r�r
        return True

    # Ge�erli koordinattan sonraki t�m hareketleri dene x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        #print(new_x,"  ",new_y)

        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            #print(new_x, "  ", new_y)
            #print()
            if (solveKTUtil(board, new_x, new_y, move_x, move_y, pos + 1)):

                return True

            else:
           

                board[new_x][new_y] = -1
            
    return False

solveKT()