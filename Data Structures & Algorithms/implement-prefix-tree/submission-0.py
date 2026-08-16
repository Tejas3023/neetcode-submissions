class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
class PrefixTree:


    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.links[i] == None:
                curr.links[i] = TrieNode()
            curr = curr.links[i]
        curr.flag = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.links[i] == None:
                return False
            curr = curr.links[i]
        return curr.flag

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.links[i] == None:
                return False
            curr = curr.links[i]
        return True
        
        