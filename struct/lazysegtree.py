from math import log2, ceil
class LazySegTree:

    #Implementation of lazy segment tree

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
        self.lazy = [initial for i in range(2*2**self.h)]
        self.func = func

    #Lazily evaluate the given index
    #Helper function
    def eval(self,idx):
        if self.lazy[idx]==self.initial:
            return
        if self.ridx[idx]!=self.lidx[idx]:
            self.lazy[idx*2] = self.func(self.lazy[idx*2],self.lazy[idx])
            self.lazy[idx*2+1] = self.func(self.lazy[idx*2+1],self.lazy[idx])
        self.tree[idx] = self.func(self.lazy[idx],self.tree[idx])
        #print(idx,self.lazy[idx],self.tree[idx])

        #print(self.tree)
        self.lazy[idx] = self.initial
        return


    #Update the tree with value x between [i,j]
    #1-index indicies should be given
    def update(self,i,j,x):
        q = [1]
        q2 = []
        while q:
            cur = q.pop()
            q2.append(cur)
            self.eval(cur)
            if self.lidx[cur]>=i and self.ridx[cur]<=j:
                self.lazy[cur] = x
                self.eval(cur)
            else:
                if self.ridx[cur*2]>=i:
                    q.append(cur*2)
                if self.lidx[cur*2+1]<=j:
                    q.append(cur*2+1)
        while q2:
            cur = q2.pop()
            if not (self.lidx[cur]>=i and self.ridx[cur]<=j):
                self.tree[cur] = self.func(self.tree[cur*2],self.tree[cur*2+1])
        return


    #Get the segment between [i,j]
    #Since the "initial" value declared at the constructer will be used,
    #Make sure that the appropriate initial is selected.
    #Example: 2**63 for min, -2**63 for max
    def get(self,i,j):
        q = [1]
        q2 = []
        ans = self.initial
        while q:
            cur = q.pop()
            self.eval(cur)
            q2.append(cur)
            if not(self.lidx[cur]>=i and self.ridx[cur]<=j):
                if self.ridx[cur*2]>=i:
                    q.append(cur*2)
                if self.lidx[cur*2+1]<=j:
                    q.append(cur*2+1)
        while q2:
            cur = q2.pop()
            ans = self.func(ans,self.tree[cur])
        return ans


    #Get methods for tree and lazy tree
    def getTree(self):
        return self.tree
    def getLazy(self):
        return self.lazy
