class UnionFind:

    #Constructer: n is the size of union-find tree desired
    def __init__(self,n):
        self.n = n
        self.rank = [1 for i in range(n)]
        self.root = [i for i in range(n)]

    #Returns the root of idx i. Compresses path while doing so
    def findroot(self,i):
        q = []
        while self.root[i]!=i:
            q.append(i)
            i = self.root[i]
        for j in q:
            self.root[j] = i
        return  i

    #Unifies trees containing idx i and idx j
    #Uses rank to decide the parent tree
    def union(self,i,j):
        if self.findroot(i)==self.findroot(j):
            return
        if self.rank[self.root[i]]>self.rank[self.root[j]]:
            self.root[self.root[j]] = self.root[i]
        elif self.rank[self.root[i]]<self.rank[self.root[j]]:
            self.root[self.root[i]] = self.root[j]
        else:
            self.root[self.root[j]] = self.root[i]
            self.rank[self.root[i]] += 1
        return

    #Returns true if idx i and idx j are in the same tree, false otherwise
    def find(self,i,j):
        return self.findroot(i)==self.findroot(j)
