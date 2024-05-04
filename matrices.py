import copy

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
                    dps[i][j].append([[i,j],[i-1,j+1],[i-2,j-2],[i-3,j-3]])
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









                    



