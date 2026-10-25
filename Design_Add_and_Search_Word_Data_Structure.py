# Design a data structure that supports adding new words and searching for existing words.

# Implement the WordDictionary class:

# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# Example 1:

# Input:
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]

# Output:
# [null, null, null, null, false, true, true, true]

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.end = True
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return True
            w = word[i]
            if w == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
            if w not in node.children:
                return False
            return dfs(node.children[w], i + 1)
        return dfs(self.root, 0)
            
if __name__=='__main__':
    WordDictionary = WordDictionary()
    print(WordDictionary.addWord("day"))
    print(WordDictionary.addWord("bay"))
    print(WordDictionary.addWord("may"))
    print(WordDictionary.search("say")) # return false
    print(WordDictionary.search("day")) # return true
    print(WordDictionary.search(".ay")) # return true
    print(WordDictionary.search("b..")) # return true

        

