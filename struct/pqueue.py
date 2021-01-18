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
