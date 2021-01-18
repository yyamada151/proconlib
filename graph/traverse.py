#Library for graph traveersal
#Unless specified, all graphs must be and will be represented by 0-index adjacency list

#Priority queue
#Implementation based on:
#https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate/8875823

import heapq

class PQueue:

    #Assumes each item to be of a tuple or list with [key,item]
    def __init__(self,init=None,key=lambda x:x[0]):
        self.tokey = key
        self.idx = 0
        self.data = []
        if init:
            self.data = [(key(item),i,item) for i,item in enumerate(init)]
            self.idx = len(self.data)
            heapq.heapify(self.data)

    def push(self,item):
        heapq.heappush(self.data,(self.tokey(item),self.idx,item))
        self.idx += 1

    def pop(self):
        return heapq.heappop(self.data)[2]

    def size(self):
        return len(self.data)

    def peek(self):
        if self.data:
            return self.data[0][2]
        else:
            return None

    def pushpop(self,item):
        val = heapq.heappushpop(self.data,(self.tokey(item),self.idx,item))
        self.idx += 1
        return val

#Dijkstra's method
#Returns the distance from provided index
#Expects each edge to be represented as [distance,destination]
def dijkstra(g,source):
    d = [2**63 for i in range(len(g))]
    d[source] = 0
    pq = PQueue()
    count = 0
    visited = 1
    for i in g[source]:
        pq.push(i)
        count += 1
    while visited<n and count>0:
        cur = pq.pop()
        count -= 1
        if d[cur[1]]<2**63:
            continue
        visited += 1
        d[cur[1]] = cur[0]
        for i in g[cur[1]]:
            if d[i[1]]<2**63:
                continue
            count += 1
            pq.push([i[0]+cur[0],i[1]])
    return d 
