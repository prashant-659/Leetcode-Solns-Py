class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26
#         self.end = False


# class Trie:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         curr = self.root
#         for c in word:
#             i = ord(c) - ord("a")
#             if curr.children[i] == None:
#                 curr.children[i] = TrieNode()
#             curr = curr.children[i]
#         curr.end = True

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         curr = self.root
#         for c in word:
#             i = ord(c) - ord("a")
#             if curr.children[i] == None:
#                 return False
#             curr = curr.children[i]
#         return curr.end

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         curr = self.root
#         for c in prefix:
#             i = ord(c) - ord("a")
#             if curr.children[i] == None:
#                 return False
#             curr = curr.children[i]
#         return True


