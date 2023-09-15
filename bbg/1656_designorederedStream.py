class OrderedStream:

    def __init__(self, n: int):
        self.array = [""] * (n + 1)
        self.curidx = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey] = value
        return_arr = []
        while True:
            if self.curidx > self.n:
                break
            if self.array[self.curidx] != "":
                return_arr.append(self.array[self.curidx])
                self.curidx += 1
            else:
                break

        return return_arr
         


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

