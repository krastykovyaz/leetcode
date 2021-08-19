from typing import List

class Solution:
    def FindAnagram(self, strs: List[List]):
        anagram = {}
        if strs == '':
            return [['']]
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word not in anagram:
                anagram[sorted_word] = [word]
            else:
                anagram[sorted_word].append(word)
        anagram_list = []
        for k,v in anagram.items():
            anagram_list.append(v)
        return anagram_list



if __name__=='__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.FindAnagram(strs))