
#Computes a^n%mod
#Cost: O(log(n))
#Input parameters:
#a: int. base of the exponent
#n: int. power
#mod: int. the value of modulus to be returned
#Returns:
#m: int. a^n%mod
def modpower(a,n,mod):
    m = 1
    while n>0:
        if n & 1:
            m *= a
            m %= mod
        a *= a
        a %= mod
        n >>= 1
    return m

#Generates an array containining mod-inverse
#Cost: O(n)
#Input parameters:
#n: int. the size of the array desired
#mod: int. the modulus to be used
#Returns:
#invlist: list. invlist[i] contains the mod-inverse of i
def getinvlist(n,mod):
    invlist = [1,1]
    for i in range(2,n+1):
        invlist.append(mod-((mod//i)*invlist[mod%i]%mod))
    return invlist
