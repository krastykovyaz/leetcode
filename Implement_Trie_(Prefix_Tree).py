# A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

# Implement the PrefixTree class:

# PrefixTree() Initializes the prefix tree object.
# void insert(String word) Inserts the string word into the prefix tree.
# boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# Example 1:

# Input:
# ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

# Output:
# [null, null, true, false, true, null, true]

# Explanation:
# PrefixTree prefixTree = new PrefixTree();
# prefixTree.insert("dog");
# prefixTree.search("dog");    // return true
# prefixTree.search("do");     // return false
# prefixTree.startsWith("do"); // return true
# prefixTree.insert("do");
# prefixTree.search("do");     // return true

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

        

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
       
        
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_end = True
        



    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.is_end
        

        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True
        


if __name__=='__main__':
    prefixTree = PrefixTree()
    print(prefixTree.insert("dog"))
    # print(prefixTree.root.children)
    print(prefixTree.search("dog"))
    print(prefixTree.search("do"))
    print(prefixTree.startsWith("do"))
    print(prefixTree.insert("do"))
    print(prefixTree.search("do"))
        
        