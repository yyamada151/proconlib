class Combination:

    #Creates a combination object
    #Using this object, one can compute factorials, combinations divided by provided modulus in O(1) time

    #n: the maximal size of factorials to be computed
    #mod: the modulus with which the factorial is divided by
    def __init__(self,n,mod):
        if n<0:
            raise ValueError("n cannot be negative")
        self.n = n
        self.mod = mod
        self.factorials = [1]
        for i in range(n):
            self.factorials.append((self.factorials[-1]*(i+1))%mod)
        self.inv = [1,1]
        for i in range(1,n):
            self.inv.append(mod-self.inv[mod%(i+1)]*(mod//(i+1))%mod)
        self.finv = [1,1]
        for i in range(1,n):
            self.finv.append((self.finv[i]*self.inv[i+1])%mod)

    def update(self,j):
        while self.n<j:
            self.n += 1
            self.factorials.append((factorials[-1]*(self.n+1))%self.mod)
            self.inv.append(self.mod-inv[self.mod%(self.n+1)]*(self.mod//(self.n+1))%self.mod)
            self.finv.append((self.finv[self.n]*self.inv[self.n+1])%self.mod)

    #Computes m!
    def fact(self,m):
        if m>self.n:
            update(m)
        return self.factorials[m]

    #Computes m choose k
    def comb(self,m,k):
        if m<0 or k<0 or m<k:
            return 0
        return (self.factorials[m]*(self.finv[m-k]*self.finv[k])%self.mod)%self.mod
