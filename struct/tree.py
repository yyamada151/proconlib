#Returns the arrays containing the indicies for the left and right children of a binary tree
#h: the height of the tree desired 
def generateIdx(h):
    lidx = [-1,1]
    ridx = [-1,2**h]
    for i in range(2,2**(h+1)):
        if i%2:
            lidx.append(ridx[-1]+1)
            ridx.append(ridx[i//2])
        else:
            lidx.append(lidx[i//2])
            ridx.append((ridx[i//2]-lidx[i//2]+1)//2+lidx[i//2]-1)
    return lidx,ridx
