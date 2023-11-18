#there's AVL (balancing factor: The height of the left subtree and the height of the right subtree of each node differ by at most 1.), 
#redblack, very node is colored, either red or black.
# Root node is always black.
# No two adjacent red nodes.
# Black height is the same for all paths.
#splay (for amortized)


#here, we can access in order also bcs

from sortedcontainers import SortedList
#we get o(logn) search, insert delete
#thanks to self-balanced BST in SortedList

#why logn? cos height of the tree will always be logn

class MRUQueue:

    def __init__(self, n: int):
        temparr = [(i-1,i) for i in range(1, n+1)]
        self.sortedList = SortedList(temparr)
        self.counter = n
        

    def fetch(self, k: int) -> int:
        (idx,ans) = self.sortedList[k-1]
        SortedList.remove(self.sortedList, (idx,ans))
        SortedList.add(self.sortedList, (self.counter, ans))
        self.counter += 1
        return ans

        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)