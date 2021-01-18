from math import log2, ceil
class SegTree:

    #Implementation of non-lazy segment tree

    #Helper method to generate the left/right indicies of the segment contained by the node
    def generateIdx(self,h):
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

    #Constructer: size:
    #size: number of elements to put into
    #func: the function used to comapre elements
    #initial: the initial values stored in the tree
    #make sure to use large initial when using func such as min()
    def __init__(self,size,func,initial=0):
        self.h = ceil(log2(size))
        self.initial = initial
        self.lidx,self.ridx = self.generateIdx(self.h)
        self.tree = [initial for i in range(2*2**self.h)]
        self.func = func

    #Update the tree with value x at index i
    #1-index indicies should be given
    def update(self,i,x):
        i += 2**self.h - 1
        self.tree[i] = self.func(self.tree[i],x)
        while i>1:
            i //= 2
            self.tree[i] = self.func(self.tree[i*2],self.tree[i*2+1])
        return

    #Get the segment between [i,j]
    def get(self,i,j):
        q = [1]
        ans = self.initial
        while q:
            cur = q.pop()
            if self.lidx[cur]>=i and self.ridx[cur]<=j:
                ans = self.func(self.tree[cur],ans)
            else:
                if self.ridx[cur*2]>=i:
                    q.append(cur*2)
                if self.lidx[cur*2+1]<=j:
                    q.append(cur*2+1)
        return ans

    #Get tree array
    def getTree(self):
        return self.tree
