import interfaces
import copy 
from interfaces import Token

l_b = []
at = Token.EMPTY
ne =0 
nr = 0 
ny = 0 

n = 0
p = 0
an = 0 
ap = 0

posr = []
posy = []

pr = 0 
py = 0 

dh = [[j for i in range(7)] for j in range(6) ]
dhp = [[j for i in range(7)] for j in range(5,-1,-1)]
dv = [[i for i in range(7)] for j in range(6) ]
dvp = [[i for i in range(6,-1,-1) ] for j in range(6)]
dp = [[[] for i in range(7)] for j in range(6)]
dps = [[[] for i in range(7)] for j in range(6)]


def mp(arg):
    for i in arg:
        print(i,"\n")


def calc_m():
    global dps, dv,dh,diag1,diag2

    dv = [[j for i in range(7)] for j in range(6) ]
    dvp = [[j for i in range(7)] for j in range(5,-1,-1)]
    dh = [[i for i in range(7)] for j in range(6) ]
    dhp  = [[i for i in range(6,-1,-1) ] for j in range(6)]
    dm = [[min(dh[j][i], dv[j][i], dhp[j][i],dvp[j][i]) for i in range(7) ] for j in range(6) ]
    dmm = [[1 for i in range(7) ] for j in range(6) ]
    dmp = [[max(dh[j][i], dv[j][i]) for i in range(7) ] for j in range(6) ]

    diag1 = [[1,1,1,1,0,0,0],[1,2,2,2,1,0,0],[1,2,3,3,2,1,0],[0,1,2,3,3,2,1],[0,0,1,2,2,2,1],[0,0,0,1,1,1,1]]
    diag2 = copy.deepcopy(diag1)
    for sub in diag2: 
        sub.reverse()


    dmm[1][5] = 0 
    dmm[0][5] = 0
    dmm[0][6] = 0 
    dmm[1][6] = 0 

    dmm[4][1] = 0
    dmm[4][0] = 0 
    dmm[5][1]= 0
    dmm[5][0]= 0 
    def mp(arg): 
        for i in arg:
            print(i,"\n")

    dp = [[[] for j in range(7)] for i in range(6)]
    dps = [[[] for j in range(7)] for i in range(6)]

    for i in range(len(dp)):
        for j in range(len(dp[i])):
                """
                dp[i][j].append(dh[i][j])
                dp[i][j].append(dhp[i][j])
                dp[i][j].append(dv[i][j])
                dp[i][j].append(dvp[i][j])
                """
                # 1 , la ligne , 2 la colonne , 3 série, 4 la position ,5 le x 
                # les séries verticales 
                if dv[i][j] == 0:
                    dps[i][j].append([[i,j],[i+1,j],[i+2,j],[i+3,j]])
                elif dv[i][j] == 1:
                    dps[i][j].append([[i,j],[i+1,j],[i+2,j],[i+3,j]])
                    dps[i][j].append([[i-1,j],[i,j],[i+1,j],[i+2,j]])
                elif dv[i][j] == 2:
                    dps[i][j].append([[i,j],[i+1,j],[i+2,j],[i+3,j]])
                    dps[i][j].append([[i-1,j],[i,j],[i+1,j],[i+2,j]])
                    dps[i][j].append([[i-2,j],[i-1,j],[i,j],[i+1,j]])
                elif dv[i][j] == 3:
                    dps[i][j].append([[i-1,j],[i,j],[i+1,j],[i+2,j]])
                    dps[i][j].append([[i-2,j],[i-1,j],[i,j],[i+1,j]])
                    dps[i][j].append([[i-3,j],[i-2,j],[i-1,j],[i,j]])
                elif dv[i][j] == 4:
                    dps[i][j].append([[i-2,j],[i-1,j],[i,j],[i+1,j]])
                    dps[i][j].append([[i-3,j],[i-2,j],[i-1,j],[i,j]])
                elif dv[i][j] == 5:
                    dps[i][j].append([[i-3,j],[i-2,j],[i-1,j],[i,j]])
                #les séries horizontales
               
                if dh[i][j] == 0:
                    dps[i][j].append([[i,j],[i,j+1],[i,j+2],[i,j+3]])
                if dh[i][j] == 1:
                    dps[i][j].append([[i,j],[i,j+1],[i,j+2],[i,j+3]])
                    dps[i][j].append([[i,j-1],[i,j],[i,j+1],[i,j+2]])
                if dh[i][j] == 2:
                    dps[i][j].append([[i,j],[i,j+1],[i,j+2],[i,j+3]])
                    dps[i][j].append([[i,j-1],[i,j],[i,j+1],[i,j+2]])
                    dps[i][j].append([[i,j-2],[i,j-1],[i,j],[i,j+1]])
                if dh[i][j] ==3:
                    dps[i][j].append([[i,j],[i,j+1],[i,j+2],[i,j+3]])
                    dps[i][j].append([[i,j-1],[i,j],[i,j+1],[i,j+2]])
                    dps[i][j].append([[i,j-2],[i,j-1],[i,j],[i,j+1]])
                    dps[i][j].append([[i,j-3],[i,j-2],[i,j-1],[i,j]])
                if dh[i][j]    == 4:
                    dps[i][j].append([[i,j-1],[i,j],[i,j+1],[i,j+2]])
                    dps[i][j].append([[i,j-2],[i,j-1],[i,j],[i,j+1]])
                    dps[i][j].append([[i,j-3],[i,j-2],[i,j-1],[i,j]])
                if dh[i][j]== 5:
                    dps[i][j].append([[i,j-2],[i,j-1],[i,j],[i,j+1]])
                    dps[i][j].append([[i,j-3],[i,j-2],[i,j-1],[i,j]])
                if dh[i][j]== 6:
                    dps[i][j].append([[i,j-3],[i,j-2],[i,j-1],[i,j]])
                

                #poour les diagnonale descendante (haut gauche bas droite )
                if diag1[i][j] == 1:
                    if dh[i][j]==0 or dv[i][j]==0 : 
                        dps[i][j].append([[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]])
                    if (dh[i][j]==1 and dv[i][j]== 3) or (dh[i][j]== 4 and dv[i][j]== 1):
                        dps[i][j].append([[i-1,j-1],[i,j],[i+1,j+1],[i+2,j+2]])
                    if (dh[i][j]== 2 and dv[i][j] == 4 ) or (dh[i][j] == 5 and dv[i][j] == 2 ): 
                        dps[i][j].append([[i-2,j-2],[i-1,j-1],[i,j],[i+1,j+1]])
                    if dh[i][j] == 6 or dv[i][j] == 5 : 
                        dps[i][j].append([[i-3,j-3],[i-2,j-2],[i-1,j-1],[i,j]])
                if diag1[i][j]== 2: 
                    if dh[i][j] == 1 or dv[i][j]== 1 :
                        dps[i][j].append([[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]])
                        dps[i][j].append([[i-1,j-1],[i,j],[i+1,j+1],[i+2,j+2]])
                    if (dh[i][j] == 2 or dv[i][j]== 3 ) and (dh[i][j] == 4 and dv[i][j]== 2):
                        dps[i][j].append([[i-1,j-1],[i,j],[i+1,j+1],[i+2,j+2]])
                        dps[i][j].append([[i-2,j-2],[i-1,j-1],[i,j],[i+1,j+1]])
                    if dh[i][j] == 5  or dv[i][j]== 4 : 
                        dps[i][j].append([[i-2,j-2],[i-1,j-1],[i,j],[i+1,j+1]])
                        dps[i][j].append([[i-3,j-3],[i-2,j-2],[i-1,j-1],[i,j]])
                if diag1[i][j] == 3 : 
                    if dv[i][j] == 2 : 
                        dps[i][j].append([[i-2,j-2],[i-1,j-1],[i,j],[i+1,j+1]])
                        dps[i][j].append([[i-1,j-1],[i,j],[i+1,j+1],[i+2,j+2]])
                        dps[i][j].append([[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]])
                    if dv[i][j] == 3 : 
                        dps[i][j].append([[i-3,j-3],[i-2,j-2],[i-1,j-1],[i,j]])
                        dps[i][j].append([[i-2,j-2],[i-1,j-1],[i,j],[i+1,j+1]])
                        dps[i][j].append([[i-1,j-1],[i,j],[i+1,j+1],[i+2,j+2]])

                #les diagonales gauches:bas - droite:haut 

                if diag2[i][j]== 1 : 
                    if dh[i][j]== 0 or dv[i][j]== 5 : 
                        dps[i][j].append([[i,j],[i-1,j+1],[i-2,j+2],[i-3,j+3]])
                    if (dh[i][j] == 4 and dv[i][j]== 4 ) or (dh[i][j]== 1 and dv[i][j]== 2): 
                        dps[i][j].append([[i + 1 , j -1],[i,j],[i-1, j + 1 ],[i-2,j + 2 ]])
                    if (dh[i][j]== 2 and dv[i][j] == 1 ) or (dh[i][j]== 5 and dv[i][j]== 3): 
                        dps[i][j].append([[i+2,  j-2],[i+1,j-1],[i,j],[i-1,j+1]])
                    if dh[i][j]== 6  or dv[i][j]== 0 :
                        dps[i][j].append([[i+3,j-3],[i+2,j-2],[i+1,j-1],[i,j]])
                if diag2[i][j]== 2 : 
                    if dh[i][j]== 1 or dv[i][j] == 4:
                        dps[i][j].append([[i+1,j-1],[i,j],[i-1,j+1],[i-2,j+2]])
                        dps[i][j].append([[i,j],[i-1,j+1],[i-1,j+2],[i-3,j+3]])

                    if (dh[i][j] == 2 and dv[i][j]== 1 ) or (dh[i][j]== 4 and dv[i][j]== 3 ) :
                        dps[i][j].append([[i+2,j-2],[i+1,j-1],[i,j],[i-1,j+1]])
                        dps[i][j].append([[i+1,j-1],[i,j],[i-1,j+1],[i-2,j+2]])
                    if dh[i][j]== 5 or dv[i][j]== 1 :
                        dps[i][j].append([[i+3,j-3],[i+2,j-2],[i + 1 , j -1 ], [i,j]])
                        dps[i][j].append([[i+2,j-2],[i+1,j-1],[i,j],[i-1,j+1]])

                if diag2[i][j]== 3 : 
                    if dv[i][j]== 3 : 
                        dps[i][j].append([[i+2,j-2],[i+1,j-1],[i,j],[i-1,j+1]])
                        dps[i][j].append([[i+1,j-1],[i,j],[i-1,j+1],[i-2,j+2]])
                        dps[i][j].append([[i,j],[i-1,j+1],[i-1,j+2],[i-3,j+3]])
                    if dv[i][j]== 2 : 
                        dps[i][j].append([[i+3,j-3],[i+2,j-2],[i + 1 , j -1 ], [i,j]])
                        dps[i][j].append([[i+2,j-2],[i+1,j-1],[i,j],[i-1,j+1]])
                        dps[i][j].append([[i+1,j-1],[i,j],[i-1,j+1],[i-2,j+2]])





def calc_mb(b): 
    mb = [[b.column(j)[i] for j in range(7)] for i in range(6)]
    return mb

def calc_pos(m_b):
    posr = []
    posy = []
    r = Token.RED
    y = Token.YELLOW

    # Parcourir chaque sous-array dans la matrice m_b
    for i, sous_array in enumerate(m_b):
        for j, valeur in enumerate(sous_array):
            # Vérifier la valeur et ajouter la position à la liste correspondante
            if valeur == r:
                posr.append([i, j])
            elif valeur == y:
                posy.append([i, j])
    return [posr,posy]

def calc_p(po, po_a): 
    p = 0 
    for i in po:
        for j in dps[i[0]][i[1]]:
            b = 1 
            

            for k in j:
                if k in po_a: 
                    b = 0 
                    break
            if b == 1:
                p += 1 

    return p
                        



   


class GroupeDavidStrategy(interfaces.Strategy):
    global ne, nr, ny, posr, posy, pose, pr, py , l_b

 

    """
    Strategy that plays a valid random move for each play.
    """



    def authors(self) -> str:
        return "Alexis Rosenfeld, David Simonet"

    def play(self, b: interfaces.Board, t: interfaces.Token) -> int:
        global ne, nr, ny, posr, posy, pose, pr, py, at , stra, apos, pos, l_b
        stra = ""
        r = Token.RED
        y = Token.YELLOW
        e = Token.EMPTY
        # playable_columns = [index for index in range(current_board.width) if
        #                     interfaces.Token.EMPTY in current_board.column(index)]
        # secrets.choice(playable_columns)
        mb = calc_mb(b) 
        b_p = [[[] for _ in range(6)] for _ in range(7)]


        def reverse_nested_list(arr):
            reversed_arr = [sub_arr[::-1] for sub_arr in arr]
            return reversed_arr

        # Reverse each sub-array (row) in the nested list
        i_m_b = reverse_nested_list(mb)

        width = len(mb[0])
        height = len(mb)

        # print(m_b[0][0])
        # print(m_b[2][0])
        # print(m_b[2][1])

        nr = 0
        ny = 0
        ne = 0

        



        # Parcourir chaque tableau dans la matrice m_b
        for sous_array in mb:
            for valeur in sous_array:
                # Incrémenter le compteur correspondant à la valeur
                if valeur == r:
                    nr += 1
                elif valeur == y:
                    ny += 1
                elif valeur == e:
                    ne += 1

    

        # print(b)
        # print(nr)
        # print(ny)
        # print(ne)
        # print(positions_r)

       
        calc_m()

       
        l_b = [[b,[0]]]

        

        

       


       

        
        


        return 1

stra = GroupeDavidStrategy()
