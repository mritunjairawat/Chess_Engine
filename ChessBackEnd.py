import numpy as np

#####################
# CHESS BOARD 
board=np.zeros((8,8,2))

########################
#  CHESS PIECES CODE
#  1. Pawns   #  2. horse
#  3. bishop  #  4. rook
#  5. queen   #  6. king

## White pieces are positive and Black pieces are negitive


##########################
##  BOARD INITIALIZER 
def init_board(brd):
    
    ## Place rook
    for i in range(8):
        brd[1][i]=1
        brd[6][i]=-1
    brd[0][1]=2
    brd[7][1]=-2
    brd[0][6]=2
    brd[7][6]=-2

    brd[0][2]=3
    brd[7][2]=-3
    brd[0][5]=3
    brd[7][5]=-3

    brd[0][0]=4
    brd[7][0]=-4
    brd[0][7]=4
    brd[7][7]=-4

    brd[0][3]=5
    brd[7][3]=-5

    brd[0][4]=6
    brd[7][4]=-6


