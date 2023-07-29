#key things -> need bfs bcs more than one path of dot
#rmbr writing dfs stuff, only return True if hv true
#if go through all possible calls and no trues, then return False after

class TrieNode():
    def __init__(self):
        self.endWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        cur = self.root

        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]

        cur.endWord = True


    # we need dfs here bcs? we could go down more than
    #one path bcs of the dot
    
    def search(self, word: str) -> bool:

        def dfs(idx, node):

            if idx >= len(word):
                return node.endWord

            cur = node

            letter = word[idx]

            #dfs paths
            if letter == ".":
                if len(cur.children) == 0:
                    return False

                #rmbr? go through everything first, then if there's something true
                #return it. else just zam false

                else:
                    for key, val in cur.children.items():
                        if dfs(idx+1, val):
                            return True
                    return False

            else:
                if letter not in cur.children:
                    return False

                return dfs(idx+1, node.children[letter])

        return dfs(0, self.root)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)