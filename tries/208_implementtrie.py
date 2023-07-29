class TrieNode:
    def __init__(self):
        self.endWord = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        #start picking from top of tree
        cur = self.root
        
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()

            cur = cur.children[letter]

        #once done iterating
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]

        return cur.endWord
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]

        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)