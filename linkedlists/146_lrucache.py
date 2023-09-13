class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None
         


#LRU <-> NODE  <-> NODE <-> NODE <-> MRU

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.nxt = self.MRU
        self.MRU.prev = self.LRU


    #always insert this next to MRU
    def insert(self, thisnode):
        tmp = self.MRU.prev
        tmp.nxt = thisnode
        thisnode.prev = tmp
        thisnode.nxt = self.MRU
        self.MRU.prev = thisnode
        
    #remove node from whenever it is
    def remove(self, thenode):
        nodebefore = thenode.prev
        nodeafter = thenode.nxt
        nodebefore.nxt = nodeafter
        nodeafter.prev = nodebefore

    def get(self, key: int) -> int:
        #returns the val of the key if key exists, otherwise return -1
        if key not in self.hashmap:
            return -1
        else:
            #return the value of the key
            #move this to MRU
            thisnode = self.hashmap[key]
            ans = thisnode.val
            self.remove(thisnode)
            self.insert(thisnode)
            return ans

    def put(self, key: int, value: int) -> None:
        #if exists in cache already:
        if key in self.hashmap:
            thenode = self.hashmap[key]
            thenode.val = value
            self.remove(thenode)
            self.insert(thenode)

        else:
            #kickingout
            if len(self.hashmap) >= self.capacity:
                removalnode = self.LRU.nxt
                del self.hashmap[removalnode.key]
                self.remove(removalnode)

                thisnode = Node(key, value)
                self.hashmap[key] = thisnode
                self.insert(thisnode)
               
            #just add
            else:
                thisnode = Node(key, value)
                self.insert(thisnode)
                self.hashmap[key] = thisnode


        #check length of current cache

        #if length above k, kick out node right next to LRU

        #insert at MRU
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)