#take note of indexing + swopping wtv needs to be swopped.
#rmbr to delete idx of an idx of a lsit in o(1), swop to end and pop.
#but u need to know which idx la. so can keep track in hashmap


class RandomizedSet:

    def __init__(self):
        self.val_idx_dict = {}
        self.values = []
        
        

    def insert(self, val: int) -> bool:

            #if not in dict
                #append to values
                #add to dict, last indexes
                #return true

            #in dict
                #return false

        if val not in self.val_idx_dict:
            self.values.append(val)
            self.val_idx_dict[val] = len(self.values) - 1
            return True

        else:
            return False

        
    def remove(self, val: int) -> bool:

        #if not in dict
            #return false

        #else
            #get idx of that element in dict
            #swop end and that element
            #change idx of swopped element in dict
            #pop from indexes

            #return true

        if val not in self.val_idx_dict:
            return False

        else:
            # print(self.values)
            # print(self.val_idx_dict)
            if len(self.values) == 1:
                del self.val_idx_dict[self.values[-1]]
                self.values.pop()
            else:
                #(val: 0, idx :0)
                swopidx = self.val_idx_dict[val]

                self.val_idx_dict[self.values[-1]] = swopidx

                #(val 1)
                endval = self.values[-1]

                #[0,1] becomes [1,0]
                self.values[-1] = self.values[swopidx]
                self.values[swopidx] = endval
                #swop whatever u swopped with the idx
                del self.val_idx_dict[self.values[-1]]
                self.values.pop()

            # print(self.values)
            # print(self.val_idx_dict)

            return True

    def getRandom(self) -> int:

        return self.values[random.randint(0,len(self.values)-1)]

        #randint, 0, len(end)
        #return from indexes

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#[2]