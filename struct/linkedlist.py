class linkedlist:
    def __init__(self):
        self.arr = [None]
        self.link = [0]
        self.start = 0
        self.size = 0

    #Insert the element to the front of the linked list
    #Opeartes in O(1) time
    def insert_first(self,e):
        self.arr.append(e)
        self.link.append(self.start)
        self.size += 1
        self.start = self.size

    #Insert the element in a given position, 0-index
    #Takes O(n) time
    def insert(self,e,pos):
        if not pos:
            self.insert_first(e)
        else:
            self.arr.append(e)
            self.size += 1
            idx = self.start
            for i in range(pos-1):
                idx = self.link[idx]
            link_next = self.link[idx]
            self.link[idx] = self.size
            self.link.append(link_next)

    #Returns the list ordered as the linked-list
    #Takes O(n) time
    def getlist(self):
        llist = []
        idx = self.start
        for i in range(1,self.size+1):
            llist.append(self.arr[idx])
            idx = self.link[idx]
        return llist
